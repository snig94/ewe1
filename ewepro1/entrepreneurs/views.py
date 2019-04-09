from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render
from .models import Entr_Signup
from .forms import Signup
from django.http import HttpResponseRedirect
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
			signup.product=form.cleaned_data['product']
			signup.location=form.cleaned_data['location']
			signup.email=form.cleaned_data['email']
			signup.phoneno=form.cleaned_data['phno']
			signup.username=form.cleaned_data['username']
			psw1 = form.cleaned_data['password1']
			psw2 = form.cleaned_data['password2']
			if psw1 == psw2:
				signup.password = psw1
			else:
				print ("invalid passwords")
				return render(request, 'entrepreneurs/signup.html', {'sign_up': form})
			
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
		
		user=Entr_Signup.objects.all().filter(username=username,password=password)
		if user:
			for x in user:
				request.session['id']=x.id
			return render(request,"entrepreneurs/dashboard.html")
		else:
			print ("error")
	return render(request,"entrepreneurs/index.html")

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
		phno=request.POST.get('phno','')
		print(phno)
		username=request.POST.get('username','')
		print(username)
		Entr_Signup.objects.filter(id=eid).update(name=name,email=email,phoneno=phno,username=username)
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
	return render(request,"entrepreneurs/sales.html")