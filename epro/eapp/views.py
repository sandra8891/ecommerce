from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import Gallery


# Create your views here.
def index(request):
    if request.method == 'POST' and 'image' in request.FILES:  # Ensure the 'image' key is in request.FILES
        myimage = request.FILES['image']  # Access the uploaded image from request.FILES
        # Create an instance of Gallery and save the image  # Save the object to the database
        # return redirect('index')  # Redirect back to the index page after saving
        todo123=request.POST.get("todo")
        todo321=request.POST.get("date")
        todo311=request.POST.get("course")  
        print(myimage)
        obj=Gallery(title1=todo123,title2=todo321,title3=todo311,feedimage=myimage)
        obj.save()
        data=Gallery.objects.all()
        return redirect('index')
    # Retrieve all gallery images to display
    gallery_images = Gallery.objects.all()
    return render(request, "index.html")

def sellersignup(request):
    if request.POST:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Validate form fields
        if not username or not email or not password or not confirmpassword:
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('sellerlogin')  # Redirect to login page

    return render(request, "register.html")

def sellerlogin(request):
    if 'username' in request.session:
        return redirect('index')  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            if user.is_staff:
                return redirect('index')
            return redirect('firstpage')  # Redirect to the home page
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'sellerlogin.html')

def usersignup(request):
    if request.POST:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Validate form fields
        if not username or not email or not password or not confirmpassword:
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('loginuser')  

    return render(request, "signup.html")

def loginuser(request):
    if 'username' in request.session:
        return redirect('firstpage')  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('firstpage')  
        else:
            messages.error(request, "Invalid credentials.")
            
    return render(request, 'login.html')

def firstpage(request):
    gallery_images = Gallery.objects.all()
    return render(request, "userindex.html", {
        "gallery_images": gallery_images, 
        "feeds": gallery_images  # Use the same queryset instead of querying twice
    })

def verifyotp(request):
    if request.POST:
        otp = request.POST.get('otp')
        otp1 = request.session.get('otp')
        otp_time_str = request.session.get('otp_time') 

        # Check if OTP is expired
        if otp_time_str:
            otp_time = datetime.fromisoformat(otp_time_str)  # Convert the string back to a datetime object
            otp_expiry_time = otp_time + timedelta(minutes=5)  # OTP expires after 5 minutes
            if datetime.now() > otp_expiry_time:
                messages.error(request, 'OTP has expired. Please request a new one.')
                del request.session['otp']
                del request.session['otp_time']
                return redirect('verifyotp')  # Redirect to request a new OTP

        if otp == otp1:
            del request.session['otp']
            del request.session['otp_time']
            return redirect('passwordreset')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    # Generate OTP and send email
    otp = ''.join(random.choices('123456789', k=6))
    request.session['otp'] = otp
    request.session['otp_time'] = datetime.now().isoformat()  # Store the current time as an ISO string
    message = f'Your email verification code is: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.session.get('email')]
    send_mail('Email Verification', message, email_from, recipient_list)

    return render(request, "otp.html")





def getusername(request):
    if request.POST:
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            request.session['email'] = user.email
            return redirect('verifyotp')
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('getusername')

    return render(request, 'getusername.html')


def passwordreset(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Check if the passwords match
        if confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        else:
            email = request.session.get('email')
            try:
                user = User.objects.get(email=email)

                # Set the new password
                user.set_password(password)
                user.save()

                # After resetting password, clear the session email
                del request.session['email']
                messages.success(request, "Your password has been reset successfully.")
                
                # Optionally, log the user in automatically after resetting the password
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)

                return redirect('loginuser')  # Redirect to the login page after password reset
            except User.DoesNotExist:
                messages.error(request, "No user found with that email address.")
                return redirect('getusername')  # Redirect to username input form

    return render(request, "passwordreset.html")


def logoutuser(request):
    logout(request)
    request.session.flush()
    return redirect('loginuser')
