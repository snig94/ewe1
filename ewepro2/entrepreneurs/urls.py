from django.conf.urls import url
from django.contrib import admin
from entrepreneurs import views

urlpatterns = [
   
    url(r'^$',views.home),
    url(r'^esignup/',views.esignup),
    url(r'^esignin/',views.esignin),
    url(r'^logout/',views.Logout),
    url(r'^dashboard/',views.Dashboard),
    url(r'^addprod/',views.Addprod),
    url(r'^editentrep/(?P<num>[0-3]+)/',views.Editentrep),
    url(r'^updatepaswd/',views.Updatepaswd),
    url(r'^training/',views.trainin),
    url(r'^view/',views.view),
    url(r'^product/',views.product),
    url(r'^show/',views.show),
    url(r'^buy/',views.buy),
    url(r'^pending/',views.pending),
    url(r'^sales/',views.sales),
    url(r'^approve/',views.approve),
    url(r'^asales/',views.asales),


]