from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from store.models import Store,StoreSchedule,Product,PurchaseOrder
from store.serializers import StoreSerializer,ProductSerializer,PurchaseOrderSerializer

def StoreRequest(request):
	if request.method == 'GET':
		snippets = Store.objects.all()
		serializer = StoreSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = StoreSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=200)
		return JsonResponse(serializer.errors, status=400)

def ProductRequest(request):
	if request.method == 'GET':
		snippets = Product.objects.all()
		serializer = ProductSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ProductSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=200)
		return JsonResponse(serializer.errors, status=400)

def PurchaseOrderRequest(request):
	if request.method == 'GET':
		snippets = Store.objects.all()
		serializer = PurchaseOrderSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PurchaseOrderSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)