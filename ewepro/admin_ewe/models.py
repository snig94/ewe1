from django.db import models

# Create your models here.
class admin(models.Model):
	UserName=models.CharField(max_length=50,default='')
	Password=models.CharField(max_length=50,default='')
	updationDate=models.DateTimeField(default='')
	

