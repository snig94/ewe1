from __future__ import unicode_literals
from django.shortcuts import render
from .models import admin
from customer.models import Cust_Signup
from django.http import HttpResponseRedirect

# Create your views here.
def Dashboard(request):
	return render(request,"admin/dashboard.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		
		password = request.POST['password']
		
		user=admin.objects.all().filter(UserName=username,Password=password)
		if user:
			return render(request,"admin/dashboard.html")
		else:
			print ("error")
	return render(request,"admin/index.html")

def Approve(request):
	a=Cust_Signup.objects.all().filter(status=0)
	return render(request,'admin/approve_customers.html',{'Approve_cust':a})

def Confirm(request):
	id=request.GET.get('id','')
	Cust_Signup.objects.filter(id=id).update(status=1)
	a=Cust_Signup.objects.all().filter(status=0)
	return render(request,'admin/approve_customers.html',{'Approve_cust':a})

def Logout(request):
	return HttpResponseRedirect('/admin/signin')
