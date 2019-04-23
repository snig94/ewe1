from django.conf.urls import url
from django.contrib import admin
from admin_ewe import views

urlpatterns = [
   url(r'^$',views.home),
   url(r'^dashboard/',views.home),
   url(r'^signin/',views.signin),
   url(r'^logout/',views.Logout),
   url(r'^approve/(?P<num>[0-3]+)/',views.Approve),
   url(r'^approvd/',views.Approvd),
   url(r'^confirm/(?P<num>[0-3]+)/',views.Confirm),
   url(r'^dashboard/',views.Dashboard),
   url(r'^categr/',views.Categry),
   url(r'^addpro/',views.Addpro),
   url(r'^addcat/',views.Addcat),
   url(r'^managepro/',views.Managepro),
   url(r'^editpro/(?P<num>[0-3]+)/',views.Editpro),
   url(r'^tmodule/',views.Tmodule),
   url(r'^updatepaswd/',views.Updatepaswd),
   url(r'^approve/',views.approve),
   url(r'^approved/',views.approved),
   url(r'^approv/',views.approv),
   url(r'^viewcategr/',views.viewcategry),
   url(r'^vtmodule/',views.vtmodule),
   url(r'^viewcat/',views.viewcat),
]
