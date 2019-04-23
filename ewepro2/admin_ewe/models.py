from django.db import models
from datetime import datetime,timedelta

# Create your models here.
class admin(models.Model):
	UserName=models.CharField(max_length=50,default='')
	Password=models.CharField(max_length=50,default='')
	
class Category(models.Model):
	categ=models.CharField(max_length=50,default='')
	scateg=models.CharField(max_length=50,default='')
class Addproduct(models.Model):
	productname=models.CharField(max_length=50,default='')
	productdesc=models.CharField(max_length=50,default='')
	price=models.IntegerField(default='')
	category=models.CharField(max_length=50,default='')
	quantity=models.IntegerField(default='')
	gst=models.IntegerField(default='')
	date = models.DateField(default=datetime.now())
	
	# edate = models.DateTimeField(default=datetime.now()+timedelta(days=500))
	image=models.ImageField(upload_to = 'pic_folder',default='',max_length=100)

class training(models.Model):
	Category=models.CharField(max_length=50,default='')
	Scategory=models.CharField(max_length=50,default='')
	URL=models.CharField(max_length=50,default='')
	Description=models.CharField(max_length=50,default='')
	image=models.FileField(upload_to = 'pic_folder',default='',max_length=100)

class procat(models.Model):
	Category=models.CharField(max_length=50,default='')
