from django.db import models
from datetime import datetime
# Create your models here.
class Cust_Signup(models.Model):
	name=models.CharField(max_length=50,default='')
	email=models.EmailField(max_length=50,default='')
	phoneno=models.IntegerField(default='')
	username=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=50,default='')
	

class Cust_Buy(models.Model):
	pid=models.IntegerField(default='')
	name=models.CharField(max_length=50,default='')
	description=models.CharField(max_length=50,default='')
	price=models.IntegerField(default='')
	category=models.CharField(max_length=50,default='')
	aquantity=models.IntegerField(default='')
	quantity=models.IntegerField(default='')
	tprice=models.IntegerField(default='')
	address=models.CharField(max_length=50,default='')
	phoneno=models.CharField(max_length=50,default='')
	date = models.DateField(default=datetime.now())
	adate = models.CharField(max_length=50,default='')
	image=models.FileField(upload_to = 'pic_folder',default='',max_length=100)
	status=models.BooleanField(default=False)
	cid=models.IntegerField(default='')
	eid=models.IntegerField(default='')