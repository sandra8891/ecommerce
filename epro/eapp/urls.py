from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
   path('login', views.loginuser, name='loginuser'),
    path('usersignup', views.usersignup, name='usersignup'),
    path('forgotpassword',views.getusername,name='forgotpassword'),
    path('verifyotp',views.verifyotp,name='verifyotp'),
    path('passwordreset',views.passwordreset,name='passwordreset'),
    path('gallery',views.gallery,name='gallery'),
    path('logout', views.logoutuser, name="logoutuser"),
    path('sellerlogout',views.logoutseller,name="sellerlogout"),
    path('',views.firstpage,name="firstpage"),  # Changed from 'userindex' to 'firstpage'
    path('sellerlogin',views.sellerlogin,name='sellerlogin'),
    path('sellersignup',views.sellersignup,name='sellersignup'),
    path('sellerindex',views.index,name='index'),
    path('deletion/<int:id>/', views.delete_g, name='deletion'),
    path('edit/<int:pk>/', views.edit_g, name='edit_g'),
    path('products/<int:id>',views.products,name='products'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('cview/', views.cview, name='cview'),
    path('about_us/',views.about_us,name='about_us'),
    path('home',views.home,name='home')

   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


