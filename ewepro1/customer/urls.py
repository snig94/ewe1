from django.conf.urls import url
from django.contrib import admin
from customer import views

urlpatterns = [
   
    url(r'^home/',views.home),
    url(r'^csignup/',views.csignup),
    url(r'^csignin/',views.csignin),
    url(r'^logout/',views.Logout),
    url(r'^dashboard/',views.Dashboard),
    url(r'^editcust/(?P<num>[0-3]+)/',views.Editcust),
    url(r'^updatepaswd/',views.Updatepaswd),
]