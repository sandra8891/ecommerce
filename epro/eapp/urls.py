from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.loginuser,name='loginuser'),
    path('signup', views.usersignup, name='usersignup'),
    
    
]
