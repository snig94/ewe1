from django.conf.urls import url
from django.contrib import admin
from customer import views

urlpatterns = [
   
   
    url(r'^csignup/',views.csignup),
    url(r'^csignin/',views.csignin),
    url(r'^logout/',views.Logout),
    url(r'^dashboard/',views.Dashboard),
]