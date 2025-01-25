from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('',views.loginuser,name='loginuser'),
    path('usersignup', views.usersignup, name='usersignup'),
    path('forgotpassword',views.getusername,name='forgotpassword'),
    path('verifyotp',views.verifyotp,name='verifyotp'),
    path('passwordreset',views.passwordreset,name='passwordreset'),
    path('sellerindex',views.index,name='index'),
    path('logout',views.logoutuser,name="logout"),
    path('sellerlogout',views.logoutseller,name="sellerlogout"),
    path('userindex',views.firstpage,name="firstpage"),  # Changed from 'userindex' to 'firstpage'
    path('sellerlogin',views.sellerlogin,name='sellerlogin'),
    path('sellersignup',views.sellersignup,name='sellersignup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


