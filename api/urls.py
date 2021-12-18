from django.urls import path

from .import views

urlpatterns = [
	path('api',views.index),
	path('dailyprice',views.dailyprice,name='index'),
	path('activateprice',views.activateprice),
	path('crop-price',views.cropprice), 
]