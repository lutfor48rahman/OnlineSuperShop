from django.shortcuts import render,HttpResponseRedirect,redirect

# Messages

from django.contrib import messages


# Model and forms

from AppOrder.models import Order
from AppPayment.forms import BillingAddress
from AppPayment.forms import BillingForm

from django.contrib.auth.decorators import login_required


# for Payment
# import requests
# from sslcommerz_python.payment import SSLCSession
# from decimal import Decimal
# import socket

# Create your views here.

@login_required
def checkout(request):
	saved_address = BillingAddress.objects.get_or_create(user=request.user)
	saved_address = saved_address[0]
	# save_address ar ki ki object astache ta show korbe .
	# print(saved_address)
	form = BillingForm(instance=saved_address)
	if request.method=='POST':
		form = BillingForm(request.POST,instance=saved_address)
		if form.is_valid():
			form.save()
			form = BillingForm(instance=saved_address)
			messages.success(request, f"Shipping Address Saved !")
			# return redirect('AppPayment:success')
	oreder_qs = Order.objects.filter(user=request.user, ordered=False)
	# print(oreder_qs)
	order_items = oreder_qs[0].orderitems.all()
	# print(order_item)
	order_total = oreder_qs[0].get_totals()
	return render(request,'AppPayment/checkout.html',context={'form':form,'order_items':order_items,'order_total':order_total,'saved_address':saved_address})





	@login_required
	def payment(request):
		saved_address = BillingAddress.objects.get_or_create(user=request.user)
		if not saved_address[0].is_fully_filled():
			messages.info(request,f"Please complete shipping address!")
			return redirect("AppPayment:checkout")

		if not request.user.profile.is_fully_filled():
			messages.info(request,f"Please complete profile details!")
			return redirect("AppLogin:profile")

	# 	return render(request,"AppPayment/payment.html",context={})

@login_required
def success(request):
	return render(request,'success.html')