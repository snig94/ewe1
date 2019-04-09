from django.db import models

# Create your models here.
class admin(models.Model):
	UserName=models.CharField(max_length=50,default='')
	Password=models.CharField(max_length=50,default='')
	updationDate=models.DateTimeField(default='')
class Category(models.Model):
	categ=models.CharField(max_length=50,default='')
class Addproduct(models.Model):
	productname=models.CharField(max_length=50,default='')
	productdesc=models.CharField(max_length=50,default='')
	price=models.IntegerField(default='')
	category=models.CharField(max_length=50,default='')
	quantity=models.IntegerField(default='')
	image=models.ImageField(upload_to = 'pic_folder',default='')
