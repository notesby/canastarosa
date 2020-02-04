from django.urls import path
from store import views

urlpatterns = [
	path('storeschedule/', views.StoreScheduleRequest),
    path('store/', views.StoreRequest),
    path('product/', views.ProductRequest),
    path('order/', views.PurchaseOrderRequest),
]