from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<pk>/', views.Device_details, name='Device_details'),
    #path('^/(?P<device_id>[]+)/$', views.Device_details, name='Device_details'),
]
