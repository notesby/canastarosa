from django.db import models



class Store(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class StoreSchedule(models.Model):
	class Weekdays(models.IntegerChoices):
		Monday = 1
		Tuesday = 2
		Wednesday = 3
		Thursday = 4
		Friday = 5
		Saturday = 6
		Sunday = 7
	store = models.ForeignKey(Store, 
								on_delete=models.CASCADE, 
								related_name="store_schedules")
	weekday = models.IntegerField(choices=Weekdays.choices)
	opens = models.TimeField()
	closes = models.TimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=300)
	price = models.DecimalField(max_digits=9, decimal_places=3)
	elaboration_time = models.PositiveSmallIntegerField()
	store = models.ForeignKey(Store, 
								on_delete=models.CASCADE, 
								related_name="products")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class PurchaseOrder(models.Model):
	products = models.ManyToManyField(Product)
	store = models.ForeignKey(Store, 
								on_delete=models.CASCADE, 
								related_name="purchase_orders")
	delivery_date = models.DateField()
	order_price = models.DecimalField(max_digits=12, decimal_places=3)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)