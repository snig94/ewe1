from django.conf.urls import url
from django.contrib import admin
from admin_ewe import views

urlpatterns = [
   
   url(r'^signin/',views.signin),
   url(r'^logout/',views.Logout),
   url(r'^approve/',views.Approve),
   url(r'^confirm/',views.Confirm),
   url(r'^dashboard/',views.Dashboard),
]