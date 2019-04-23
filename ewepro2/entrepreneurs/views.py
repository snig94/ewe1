from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render
from .models import Entr_Signup,Buyproduct
from .forms import Signup,pic
from admin_ewe.models import Category,training,Addproduct
from customer.models import Cust_Buy
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import datetime
# Create your views here.
def Dashboard(request):
	return render(request,"entrepreneurs/dashboard.html")
def home(request):
	return render(request,"entrepreneurs/home.html")

def esignup(request):
	if request.method=="POST":
		form=Signup(request.POST)
		if form.is_valid():
			signup=Entr_Signup()
			signup.name=form.cleaned_data['name']
			signup.cname=form.cleaned_data['cname']
			signup.description=form.cleaned_data['description']
			signup.address=form.cleaned_data['address']
			signup.email=form.cleaned_data['email']
			signup.phoneno=form.cleaned_data['phno']
			signup.username=form.cleaned_data['username']
			psw1 = form.cleaned_data['password1']
			psw2 = form.cleaned_data['password2']
			if psw1 == psw2:
				signup.password = psw1
			else:
				print ("invalid passwords")
				return render(request, 'entrepreneurs/signup.html', {'sign_up': form,'err':'Invalid Password'})
			
			signup.save()
			return HttpResponseRedirect('/entrepreneur/esignin')
		else:
			print ("inside valid else")
			print (form.errors)
		return render(request, 'entrepreneurs/signup.html', {'sign_up': form})
	else:
		print ("inside POST")
		form=Signup()
	return render(request, 'entrepreneurs/signup.html', {'sig': form})

	
def esignin(request):
	if request.method=="POST":
		username = request.POST['username']
		
		password = request.POST['password']
		
		user=Entr_Signup.objects.all().filter(username=username,password=password,status=1)
		if user:
			for x in user:
				request.session['id']=x.id
			return render(request,"entrepreneurs/dashboard.html")
		else:
			print ("error")
	return render(request,"entrepreneurs/index.html",{"suc":'Successfully added, Please wait for admin message'})

def Editentrep(request,num):
	if num=="1":
		eid=request.session['id']
		print(eid)
		eob=Entr_Signup.objects.all().filter(id=eid)
		print("________________________")
		return render(request,"entrepreneurs/edit_entrepreneurs.html",{'data':eob})
	elif num=="2":
		print('+++++++++++++++++++++')
		eid=request.session['id'] 
		# print(cid)
		name=request.POST.get('name','')
		print(name)
		email=request.POST.get('email','')
		print(email)
		cname=request.POST.get('cname','')
		phno=request.POST.get('phno','')
		print(phno)
		address=request.POST.get('address','')
		description=request.POST.get('description','')
		username=request.POST.get('username','')
		print(username)
		Entr_Signup.objects.filter(id=eid).update(name=name,email=email,cname=cname,phoneno=phno,address=address,description=description,username=username)
		eob=Entr_Signup.objects.all().filter(id=eid)

		return render(request,"entrepreneurs/edit_entrepreneurs.html",{'data':eob,'msg':"Updated successfully!! Click HOME page.."})

def Updatepaswd(request):
	if request.method=="POST":
		eid=request.session['id']
		up1=request.POST.get('password1','')
		
		up2=request.POST.get('password2','')

		if up1==up2:
			
			f=Entr_Signup.objects.filter(id=eid).update(password=up1)
			return render(request,"entrepreneurs/index.html",{'suc':'Successfully Changed Password!!! Please Login again to continue'})
		else:
			
			return render(request,"entrepreneurs/change_password.html",{'err':"Two password didn't match"})
	else:
		return render(request,"entrepreneurs/change_password.html")
def Logout(request):
	return HttpResponseRedirect('/entrepreneur/esignin')


def Addprod(request):
	c=request.session['id']
	a=Buyproduct.objects.all().filter(status=1,eid=c)
	b="Approved"
	
	return render(request,"entrepreneurs/sales.html",{'data':a,'m':b})

def trainin(request):
	a=training.objects.all()
	return render(request,'entrepreneurs/training.html',{'data':a})

def view(request):
	a=request.GET.get('id','')
	b=training.objects.all().filter(id=a)
	return render(request,"entrepreneurs/viewtraining.html",{'data':b})


def product(request):
	# r=datetime.datetime.today().strftime('%Y-%m-%d')
	# print (r)
	a=Addproduct.objects.all()
	print(a)
	return render(request,"entrepreneurs/viewproduct.html",{'data':a})

def show(request):
	a=request.GET.get('id','')
	
	
	
	
	b=Addproduct.objects.all().filter(id=a)
	print (b)
	return render(request,"entrepreneurs/productdt.html",{'data':b})

def buy(request):
	if request.method=='POST':
		print("_____________________________")
		a=request.POST.get('id','')
		idd=request.session['id']
		b=request.POST.get('name','')
		c=request.POST.get('description','')
		d=request.POST.get('price','')
		e=request.POST.get('category','')
		f=request.POST.get('aquantity','')
		g=request.POST.get('quantity','')
		h=request.POST.get('tprice','')
		i=request.POST.get('image','')
		
		k=request.POST.get('address','')
		l=request.POST.get('phone','')
		print (i)
		# imgform=pic(request.POST,request.FILES)
		# print (imgform)
		# if imgform.is_valid():
		# 	print("++++++++++++++++++++++++++++")
		# 	image=imgform.cleaned_data['image']
		if int(f)<int(g):
			n="out of stock"
			print (n)
			r=datetime.datetime.today().strftime('%Y-%m-%d')
			print (r)
			m=Addproduct.objects.all()	
			return render(request,"entrepreneurs/viewproduct.html",{'data':m,'m':n})	

		else:
			
			print ("+++++++++++++++++++++++++")
			ob=Buyproduct(Product_id=a,productname=b,productdesc=c,price=d,category=e,av_quantity=f,quantity=g,total_price=h,image=i,eid=idd,address=k,phoneno=l)
			ob.save()
			k=int(f)-int(g)
			
			Addproduct.objects.filter(id=a).update(quantity=k)
			m=Addproduct.objects.all()
		return render(request,"entrepreneurs/viewproduct.html",{'data':m})	

def pending(request):
	c=request.session['id']
	a=Buyproduct.objects.all().filter(status=0,eid=c)
	b="Pending"
	return render(request,"entrepreneurs/sales.html",{'data':a,'m':b})


def sales(request):
	b=request.session['id']
	a=Cust_Buy.objects.all().filter(status=0,eid=b)
	return render(request,"entrepreneurs/sale_product.html",{'data':a})

def approve(request):	
	b=request.GET.get('id','')
	d=datetime.datetime.now()
	dat=d.strftime("%x")
	Cust_Buy.objects.filter(id=b).update(status=1,adate=dat)
	c=request.session['id']
	a=Cust_Buy.objects.all().filter(status=0,eid=c)
	return render(request,"entrepreneurs/sale_product.html",{'data':a})


def asales(request):
	b=request.session['id']
	a=Cust_Buy.objects.all().filter(status=1,eid=b)
	return render(request,"entrepreneurs/sp.html",{'data':a})

