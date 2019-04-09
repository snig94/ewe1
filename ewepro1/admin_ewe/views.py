from django.shortcuts import render
from .models import admin,Category,Addproduct
from customer.models import Cust_Signup
from entrepreneurs.models import Entr_Signup
from django.http import HttpResponseRedirect
from .forms import Image
# Create your views here.
def Dashboard(request):
	return render(request,"admin/dashboard.html")
def home(request):
	return render(request,"admin/home.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		
		password = request.POST['password']
		
		user=admin.objects.all().filter(UserName=username,Password=password)
		if user:
			for x in user:
				request.session['id']=x.id
			return render(request,"admin/dashboard.html")
		else:
			print ("error")
	return render(request,"admin/index.html")

def Approve(request,num):
	if num=="1":
		a=Cust_Signup.objects.all().filter(status=0)
		return render(request,'admin/approve_customers.html',{'Approve_cust':a})
	else:
		b=Entr_Signup.objects.all().filter(status=0)
		return render(request,'admin/approve_entrepreneurs.html',{'Approve_entr':b})

def Confirm(request,num):
	if num=="1":
		id=request.GET.get('id','')
		Cust_Signup.objects.filter(id=id).update(status=1)
		a=Cust_Signup.objects.all().filter(status=0)
		return render(request,'admin/approve_customers.html',{'Approve_cust':a})
	else:
		id=request.GET.get('id','')
		Entr_Signup.objects.filter(id=id).update(status=1)
		a=Entr_Signup.objects.all().filter(status=0)
		return render(request,'admin/approve_entrepreneurs.html',{'Approve_entr':a})
def Categry(request):
	if request.method=="POST":
		categ=request.POST.get('category','')
		oa=Category.objects.all().filter(categ=categ)
		if oa:
			err={'error_message':'Already Added'}
			return render(request,"admin/add_categories.html",{'error':err})
		else:
			ob=Category(categ=categ)
			ob.save()
	return render(request,"admin/add_categories.html")
def Addpro(request):
	if request.method=="POST":
		
		pname=request.POST['pname']
		pdesc=request.POST['pdesc']
		price=request.POST['price']
		category=request.POST['category']
		quantity=request.POST['quantity']
		r=Addproduct.objects.all().filter(productname=pname)
		imgform=Image(request.POST,request.FILES)
		if imgform.is_valid():
			img=imgform.cleaned_data['image']
			print("--------------")
		if r.exists():
			print("++++++++++++++")
			return render(request,'admin/add_product.html',{'msg':'Already Exist'})
		else:
			print("**************")
			ap=Addproduct(productname=pname,productdesc=pdesc,price=price,category=category,quantity=quantity,image=img)
			ap.save()
			return render(request,'admin/add_product.html',{'msg1':'Added Successfully'})
	else:
		return render(request,"admin/add_product.html")
def Managepro(request):
	mp=Addproduct.objects.all()
	return render(request,"admin/manage_products.html",{'data':mp})
def Editpro(request,num):
	if num=="1":
		print("--------------")
		pid=request.GET.get('id','')
		pr=Addproduct.objects.all().filter(id=pid)
		return render(request,"admin/edit_products.html",{'prod':pr})
	else:
		print("++++++++++++++")
		
		print(pid)
		pname=request.POST['pname']
		pdesc=request.POST['pdesc']
		price=request.POST['price']
		category=request.POST['category']
		quantity=request.POST['quantity']
		imgform=Image(request.POST,request.FILES)
		if imgform.is_valid():
			img=imgform.cleaned_data['image']
			print("--------------")
			Addproduct.objects.filter(id=4).update(productname=pname,productdesc=pdesc,price=price,category=category,quantity=quantity,image=img)
			mp=Addproduct.objects.all()
			return render(request,'admin/manage_product.html',{'msg':'Updated Successfully','data':mp})
		else:
			print("++++++++++++++")
			Addproduct.objects.filter(id=4).update(productname=pname,productdesc=pdesc,price=price,category=category,quantity=quantity,image=img)
			mp=Addproduct.objects.all()
			return render(request,'admin/manage_product.html',{'msg':'Updated Successfully','data':mp})
def Updatepaswd(request):
	if request.method=="POST":
		uid=request.session['id']
		up1=request.POST.get('password1','')
		
		up2=request.POST.get('password2','')

		if up1==up2:
			
			f=admin.objects.filter(id=uid).update(Password=up1)
			return render(request,"admin/index.html",{'suc':'Successfully Changed Password!!! Please Login again to continue'})
		else:
			
			return render(request,"admin/change_password.html",{'err':"Two password didn't match"})
	else:
		return render(request,"admin/change_password.html")	

def Tmodule(request):
	return render(request,"admin/add_training.html")	
def Logout(request):
	return HttpResponseRedirect('/admin/signin')
