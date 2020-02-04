from rest_framework import serializers
from store.models import Store,StoreSchedule,Product,PurchaseOrder
from datetime import date


class StoreScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = StoreSchedule
		fields = ['id', 'weekday', 'opens', 'closes']

class StoreSerializer(serializers.ModelSerializer):
	store_schedules = StoreScheduleSerializer(many=True)
	class Meta:
		model = Store
		fields = ['id', 'name', 'slug', 'store_schedules']

	def create(self,validated_data):
		store_schedules_data = validated_data.pop('store_schedules')
		store = Store.objects.create(**validated_data)
		for store_schedules_data in store_schedules_data:
			StoreSchedule.objects.create(store=store, **store_schedules_data)
		return store

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'name', 'slug', 'price', 'store', 'elaboration_time']

class PurchaseOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = PurchaseOrder
		fields = ['delivery_date', 'store', 'order_price', 'products']

	def validate(self,data):
		products_data = data['products']
		remainingdays = (data["delivery_date"]-date.today()).days
		schedules = StoreSchedule.objects.filter(store=data["store"])
		workingdays = set([schedule.weekday for schedule in schedules])
		order_price = 0
		for product in products_data:
			#product = Product.objects.get(pk=product_id)
			order_price += product.price
			if product.elaboration_time > 0:
				if product.elaboration_time > remainingdays:
					raise serializers.ValidationError(f"Lo sentimos pero la tienda no puede entregar el pedido el dia {data['delivery_date']}")
				else:
					count = 0
					for i in range(remainingdays):
						today = date.today()
						nextDay = date(day=today.day + i,month=today.month,year=today.year)
						if nextDay.isoweekday() in workingdays:
							count += 1
					if product.elaboration_time - count > 0:
						raise serializers.ValidationError(f"Lo sentimos pero la tienda no puede entregar el pedido el dia {data['delivery_date']}")
		data["order_price"] = order_price
		return data

