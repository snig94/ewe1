from django.conf.urls import url
from django.contrib import admin
from entrepreneurs import views

urlpatterns = [
   
    url(r'^home/',views.home),
    url(r'^esignup/',views.esignup),
    url(r'^esignin/',views.esignin),
    url(r'^logout/',views.Logout),
    url(r'^dashboard/',views.Dashboard),
    url(r'^addprod/',views.Addprod),
    url(r'^editentrep/(?P<num>[0-3]+)/',views.Editentrep),
    url(r'^updatepaswd/',views.Updatepaswd),
]