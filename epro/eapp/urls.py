from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.loginuser,name='loginuser'),
    path('signup', views.usersignup, name='usersignup'),
    path('forgotpassword',views.getusername,name='forgotpassword'),
    path('verifyotp',views.verifyotp,name='verifyotp'),
    path('passwordreset',views.passwordreset,name='passwordreset'),
    path('index',views.index,name='index'),
    path('logout',views.logoutuser,name="logout")
    
    
]
