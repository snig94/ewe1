from django import forms

class Image(forms.Form):
	image= forms.ImageField()

class Files(forms.Form):
	file=forms.FileField()	
	