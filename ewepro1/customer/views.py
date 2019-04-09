from django.shortcuts import render

from django.shortcuts import render
from .models import Cust_Signup
from .forms import Signup
from django.http import HttpResponseRedirect
# Create your views here.
def Dashboard(request):
	return render(request,"customers/dashboard.html")
def home(request):
	return render(request,"customers/home.html")

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
	if request.method=="POST":
		username = request.POST['username']
		print(username)
		password = request.POST['password']
		print(password)
		user=Cust_Signup.objects.all().filter(username=username,password=password)
		print(user)
		if user:
			for x in user:
				request.session['id']=x.id
			return render(request,"customers/dashboard.html")
		else:
			print ("error")
	return render(request,"customers/index.html")
def Editcust(request,num):
	if num=="1":
		cid=request.session['id']
		print(cid)
		cob=Cust_Signup.objects.all().filter(id=cid)
		print("________________________")
		return render(request,"customers/edit_customer.html",{'data':cob})
	elif num=="2":
		print('+++++++++++++++++++++')
		cid=request.session['id'] 
		# print(cid)
		name=request.POST.get('name','')
		print(name)
		email=request.POST.get('email','')
		print(email)
		phno=request.POST.get('phno','')
		print(phno)
		username=request.POST.get('username','')
		print(username)
		Cust_Signup.objects.filter(id=cid).update(name=name,email=email,phoneno=phno,username=username)
		cob=Cust_Signup.objects.all().filter(id=cid)

		return render(request,"customers/edit_customer.html",{'data':cob,'msg':"Updated successfully!! Click HOME page.."})

def Updatepaswd(request):
	if request.method=="POST":
		uid=request.session['id']
		up1=request.POST.get('password1','')
		
		up2=request.POST.get('password2','')

		if up1==up2:
			
			f=Cust_Signup.objects.filter(id=uid).update(password=up1)
			return render(request,"customers/index.html",{'suc':'Successfully Changed Password!!! Please Login again to continue'})
		else:
			
			return render(request,"customers/change_password.html",{'err':"Two password didn't match"})
	else:
		return render(request,"customers/change_password.html")



def Logout(request):

	return HttpResponseRedirect('/customer/csignin')
