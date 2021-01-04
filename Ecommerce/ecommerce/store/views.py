from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		# Get the order for this customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		# Get all items in the order
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_item':0}

	context = {'items':items,'order':order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		# Get the order for this customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		# Get all items in the order
		items = order.orderitem_set.all()
	else:
		items == []
		order = {'get_cart_total':0,'get_cart_item':0}

	context = {'items':items,'order':order}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('ProductId',productId,'Action',action)

	customer = request.user.customer
	product = Product.object.get(id=productId)
	order, created = Order.object.get_or_create(customer=customer, complete=False)
	
	return JsonResponse('Item was added',safe=False)