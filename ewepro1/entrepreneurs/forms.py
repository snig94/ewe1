from django import forms

class Signup(forms.Form):
	name = forms.CharField(max_length = 100,required=True)
	cname = forms.CharField(max_length = 100,required=True)
	product = forms.CharField(max_length = 100,required=True)
	location = forms.CharField(max_length = 100,required=True)
	email = forms.EmailField(required=True)
	phno = forms.IntegerField(required=True)
	username = forms.CharField(max_length = 100,required=True)
	password1 = forms.CharField(max_length = 100,required=True)
	password2 = forms.CharField(max_length = 100,required=True)