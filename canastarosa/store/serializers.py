from rest_framework import serializers
from store.models import Store,StoreSchedule,Product,PurchaseOrder


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