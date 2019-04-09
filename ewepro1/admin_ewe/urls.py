from django.conf.urls import url
from django.contrib import admin
from admin_ewe import views

urlpatterns = [
   url(r'^home/',views.home),
   url(r'^signin/',views.signin),
   url(r'^logout/',views.Logout),
   url(r'^approve/(?P<num>[0-3]+)/',views.Approve),
   url(r'^confirm/(?P<num>[0-3]+)/',views.Confirm),
   url(r'^dashboard/',views.Dashboard),
   url(r'^categr/',views.Categry),
   url(r'^addpro/',views.Addpro),
   url(r'^managepro/',views.Managepro),
   url(r'^editpro/(?P<num>[0-3]+)/',views.Editpro),
   url(r'^tmodule/',views.Tmodule),
   url(r'^updatepaswd/',views.Updatepaswd),
]
