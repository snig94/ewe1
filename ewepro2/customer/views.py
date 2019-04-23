from django.shortcuts import render

from django.shortcuts import render
from .models import Cust_Signup,Cust_Buy
from .forms import Signup
from admin_ewe.models import procat
from entrepreneurs.models import Buyproduct,Entr_Signup
from django.http import HttpResponseRedirect,HttpResponse
import datetime
# Create your views here.
def Dashboard(request):
	# r=datetime.datetime.today().strftime('%Y-%m-%d')
	# print (r)
	product=Buyproduct.objects.all().filter(status=1)
	# product=Buyproduct.objects.all().filter(status=1)
	cat=procat.objects.all()
	entre=Entr_Signup.objects.all()
	
	return render(request,"customers/dashboard.html",{'data':product,'cate':cat,'entre':entre})
def home(request):
	r=datetime.datetime.today().strftime('%Y-%m-%d')
	print (r)
	product=Buyproduct.objects.all().filter(status=1)
	# product=Buyproduct.objects.all().filter(status=1)
	categ=procat.objects.all()
	entre=Entr_Signup.objects.all()
	return render(request,"customers/home.html",{'data':product,'cate':categ,'entre':entre})

def myorder(request):
	c=request.session['id']
	a=Cust_Buy.objects.all().filter(status=0,)	
	b="Pending"
	return render(request,"customers/muorder.html",{'data':a,'m':b})

def aporder(request):
	a=Cust_Buy.objects.all().filter(status=1)	
	b="Approved"
	return render(request,"customers/muorder.html",{'data':a,'m':b})

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
				
			r=datetime.datetime.today().strftime('%Y-%m-%d')
			print (r)
			product=Buyproduct.objects.all().filter(status=1)	
			# product=Buyproduct.objects.all().filter(status=1)
			cat=procat.objects.all()
			entre=Entr_Signup.objects.all()
			
			return render(request,"customers/dashboard.html",{'data':product,'cate':cat,'entre':entre})
		else:
			print ("error")
	return render(request,"customers/index.html")

def finds(request):
	p=request.GET.get('val','')	
	print ("sssssssssssssssssssssssssssssssssssssssssssssssssss")
	d=procat.objects.all().filter(id=p)
	print (d[0].Category)
	r=datetime.datetime.today().strftime('%Y-%m-%d')
	print (r)
	a=Buyproduct.objects.all().filter(category=d[0].Category,status=1)
	print (a)
		
	html=""
	for x in a:
		html +="<div class='grid1_of_4'><div class='content_box'><img src="+x.image+" class='img-responsive' style='height:150px; width:200px' alt='/> <h4><a href='View_one_product1.php?id=9'>"+x.productname+"</a></h4><p></p><div class='grid_1 simpleCart_shelfItem'><div class='item_add'><span class='item_price'><h6>ONLY Rs."+str(x.price)+"</h6></span></div><div class='item_add'><span class='item_price'><a href='/customer/buy/?id="+str(x.id)+"' >Buy Now</a></span></div></div></div></div>"
		print(x.price)
		print (html)
	return HttpResponse(html)

def efinds(request):
	p=request.GET.get('val','')	
	print ("sssssssssssssssssssssssssssssssssssssssssssssssssss")
	# d=Entr_Signup.objects.all().filter(id=p)
	# print (d[0].cname)
	r=datetime.datetime.today().strftime('%Y-%m-%d')
	print (r)
	a=Buyproduct.objects.all().filter(eid=p,status=1)
	print (a)
		
	html=""
	for x in a:
		html +="<div class='grid1_of_4'><div class='content_box'><img src="+x.image+" class='img-responsive' style='height:150px; width:200px' alt='/> <h4><a href='View_one_product1.php?id=9'>"+x.productname+"</a></h4><p></p><div class='grid_1 simpleCart_shelfItem'><div class='item_add'><span class='item_price'><h6>ONLY Rs."+str(x.price)+"</h6></span></div><div class='item_add'><span class='item_price'><a href='/customer/buy/?id="+str(x.id)+"' >Buy Now</a></span></div></div></div></div>"
		print(x.price)
		print (html)
	return HttpResponse(html)

def findlog (request):
	p=request.GET.get('val','')	
	print ("sssssssssssssssssssssssssssssssssssssssssssssssssss")
	d=procat.objects.all().filter(id=p)
	print (d[0].Category)
	r=datetime.datetime.today().strftime('%Y-%m-%d')
	print (r)
	a=Buyproduct.objects.all().filter(category=d[0].Category,status=1)
	print (a)
	msg="uuuu"	
	html=""
	for x in a:
		html +="<div class='grid1_of_4'><div class='content_box'><img src="+x.image+" class='img-responsive' style='height:150px; width:200px' alt='/> <h4><a href='View_one_product1.php?id=9'>"+x.productname+"</a></h4><p>"+x.productdesc+"</p><div class='grid_1 simpleCart_shelfItem'><div class='item_add'><span class='item_price'><h6>ONLY Rs."+str(x.price)+"</h6></span></div><div class='item_add'><span class='item_price'><a href='#' onclick='alert(`Please login to Purchase`)' >Buy Now</a></span></div></div></div></div>"
		print(x.price)
		print (html)
	return HttpResponse(html)

def buy(request):
	a=request.GET.get('id','')
	product=Buyproduct.objects.all().filter(id=a)
	return render(request,"customers/buyp.html",{'data':product})

def buyit(request):
	pid=request.POST.get('id','')
	eid=request.POST.get('eid','')
	name=request.POST.get('name','')
	description=request.POST.get('description','')
	price=request.POST.get('price','')
	category=request.POST.get('category','')
	aquantity=request.POST.get('aquantity','')
	quantity=request.POST.get('quantity','')
	tprice=request.POST.get('tprice','')
	address=request.POST.get('address','')
	phone=request.POST.get('phone','')
	image=request.POST.get('image','')
	a=request.session['id']
	if int(aquantity)<int(quantity):
			n="out of stock"
			print (n)
			product=Buyproduct.objects.all().filter(status=1)
			cat=procat.objects.all()	
			return render(request,"customers/dashboard.html",{'data':product,'cate':cat,'r':n})
	

	else:
		ob=Cust_Buy(pid=pid,name=name,description=description,price=price,category=category,aquantity=aquantity,quantity=quantity,tprice=tprice,address=address,image=image,phoneno=phone,cid=a,eid=eid)
		ob.save()
		c="order successfully"
		t=int(aquantity)-int(quantity)
		Buyproduct.objects.filter(id=pid).update(quantity=t)
		product=Buyproduct.objects.all().filter(status=1)
	
		cat=procat.objects.all()
	return render(request,"customers/dashboard.html",{'data':product,'cate':cat,'r':c})




	

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
def srch(request):
	eid=request.GET.get('val','')
	print (eid)
	r=datetime.datetime.today().strftime('%Y-%m-%d')
	print (r)
	product=Buyproduct.objects.all().filter(status=1,eid=eid)
	print (product)
	# product=Buyproduct.objects.all().filter(status=1)
	categ=procat.objects.all()
	entre=Entr_Signup.objects.all()
	return render(request,"customers/dashboard.html",{'data':product,'cate':categ,'entre':entre})


def Logout(request):

	return HttpResponseRedirect('/customer/csignin')
