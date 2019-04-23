from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime,timedelta
# Create your models here.
class Entr_Signup(models.Model):
	name=models.CharField(max_length=50,default='')
	cname=models.CharField(max_length=50,default='')
	description=models.CharField(max_length=50,default='')
	address=models.CharField(max_length=50,default='')
	email=models.EmailField(max_length=50,default='')
	phoneno=models.CharField(max_length=50,default='')
	username=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=50,default='')
	status=models.BooleanField(default=False)

class Buyproduct(models.Model):
	Product_id=models.IntegerField(default='')
	productname=models.CharField(max_length=50,default='')
	productdesc=models.CharField(max_length=50,default='')
	price=models.IntegerField(default='')
	category=models.CharField(max_length=50,default='')
	av_quantity=models.IntegerField(default='')
	quantity=models.IntegerField(default='')
	total_price=models.IntegerField(default='')
	date = models.DateField(default=datetime.now())
	apdate=models.CharField(max_length=50,default='')
	edate = models.CharField(max_length=50,default='')
	phoneno=models.CharField(max_length=50,default='')
	address=models.CharField(max_length=50,default='')
	# image=models.ImageField(upload_to = 'pic_folder',default='')
	image=models.CharField(max_length=100,default='')
	status=models.BooleanField(default=False)
	eid=models.IntegerField(default='')

