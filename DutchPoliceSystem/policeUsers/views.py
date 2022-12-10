#required imports
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Import variables from forms.py
from .forms import CreateRegistrationForm

# Import varibales from other apps
from userNotifications.models import UploadDataModel

# Import One-Time-Password Library
import pyotp

#variables declared to be used publicly

totp = pyotp.TOTP('base32secret3232')
# Create your views here.

# Define login page function
def loginPage(request):
   
    if request.method =="POST":
        #get username and password values from the login form
        usernameVal = request.POST.get('username')
        passwordVal = request.POST.get('password')
    
    
         #authenticate user
        user =authenticate(request,username=usernameVal,password=passwordVal)

        #check if user is in the databse
        if user is not None:
            
            #Generator OTP passcode
            generatedOTP()

            #verify generated OTP that has been generated
            #verifyOTP= input("enter OTP:")
            verifyOTP= input("Enter OTP: ")
            if totp.verify(verifyOTP)==True:
                login(request,user)
                return redirect('userDash')
            else:
                messages.warning(request,'Verification of OTP failed.')
                print("invalid OTP")
            
        else:
            messages.info(request,'username or password is incorrect, please try again or contact the adminstrator')

    context={}
    #renders the login page
    return render(request,'policeUsers/login.html',context)

# User registration page function
def registerPage(request):
    regForm = CreateRegistrationForm()
    #store data into the databse
    if request.method=="POST":
        regForm= CreateRegistrationForm(request.POST)
        #check if the form is valid before saving to the database
        if regForm.is_valid():
            #save details to the database
            regForm.save()

            #get first and last name of user registered
            firstName = regForm.cleaned_data.get('first_name')
            lastName = regForm.cleaned_data.get('last_name')
            name = firstName +' '+lastName

            #pass messages to the dashboard
            messages.success(request,name+' has successfully been registered and is able to login.')
            
            #redirects user to the admin dashboard (to be done later)- temporary redirection to login page
            return redirect('login')
    context = {'form':regForm}

    #renders the register page with context details
    return render(request,'policeUsers/register.html',context)

#Define logout user function
def logoutUser(request):
    logout(request)
    return redirect('login')

#Restrict the police user dashboard
@login_required(login_url='login')
def home(request):
    return render(request,'policeUsers/dashboard.html')

#Method to genrate OTP with a timer
def generatedOTP():
  #generated 6 digit OTP
  print("Your OTP is:",totp.now())



