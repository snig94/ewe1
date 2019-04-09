from django.db import models

# Create your models here.
class Cust_Signup(models.Model):
	name=models.CharField(max_length=50,default='')
	email=models.EmailField(max_length=50,default='')
	phoneno=models.IntegerField(default='')
	username=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=50,default='')
	status=models.BooleanField(default=False)
