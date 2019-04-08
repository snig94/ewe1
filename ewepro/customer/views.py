from __future__ import unicode_literals

from django.shortcuts import render
from .models import Cust_Signup
from .forms import Signup
from django.http import HttpResponseRedirect


# Create your views here.

def Dashboard(request):
	return render(request,"customers/dashboard.html")

def csignup(request):
	if request.method=="POST":
		form=Signup(request.POST)
		if form.is_valid():
			signup=Cust_Signup()
			signup.name=form.cleaned_data['name']
			signup.email=form.cleaned_data['email']
			signup.phoneno=form.cleaned_data['phno']
			signup.username=form.cleaned_data['username']
			psw1 = form.cleaned_data['password1']
			psw2 = form.cleaned_data['password2']
			if psw1 == psw2:
				signup.password = psw1
			else:
				print ("invalid passwords")
				return render(request, 'reg.html', {'sign_up': form})
			
			signup.save()
			return HttpResponseRedirect('/customer/csignin')
		else:
			print ("inside valid else")
			print (form.errors)
		return render(request, 'customers/signup.html', {'sign_up': form})
	else:
		print ("inside POST")
		form=Signup()
	return render(request, 'customers/signup.html', {'sig': form})

	
def csignin(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	ob=Cust_Signup.objects.all().filter(username=username,password=password)
	if ob:
		return render(request,"customers/dashboard.html")

	return render(request,"customers/index.html")

def Logout(request):
	return HttpResponseRedirect('/customer/csignin')
