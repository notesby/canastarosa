from rest_framework import serializers
from store.models import Store,StoreSchedule,Product,PurchaseOrder

class StoreSerializer(serializers.ModelSerializer):
		class Meta:
			model = Store
			fields = ['id', 'name', 'slug', 'store_schedules']

class StoreScheduleSerializer(serializers.ModelSerializer):
		class Meta:
			model = StoreSchedule
			fields = ['id', 'weekday', 'opens', 'closes']

class ProductSerializer(serializers.ModelSerializer):
		class Meta:
			model = Product
			fields = ['id', 'name', 'slug', 'price', 'store', 'elaboration_time']

class PurchaseOrderSerializer(serializers.ModelSerializer):
		class Meta:
			model = PurchaseOrder
			fields = ['delivery_date', 'store', 'order_price', 'products']