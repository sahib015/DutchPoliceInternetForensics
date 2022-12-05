#required imports
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#OTP Import
import pyotp

#variables declared to be used publicly

totp = pyotp.TOTP('base32secret3232')
# Create your views here.

def loginPage(request):
   
    if request.method =="POST":
        #get username and password values from the login form
        usernameVal = request.POST.get('usernameUser')
        passwordVal = request.POST.get('passwordUser')
    
    
         #authenticate user
        user =authenticate(request,username=usernameVal,password=passwordVal)

        #check if user is in the databse
        if user is not None:
            
            generatedOTP()
            #verify generated OTP that has been generated
            #verifyOTP= input("enter OTP:")
            verifyOTPUser= input("Enter OTP: ")
            if totp.verify(verifyOTPUser)==True:
                login(request,user)
                return redirect('userDash')#to be redirected to police dashboard later
            else:
                messages.warning(request,'Verification of OTP failed.')
                print("invalid OTP")
            
        else:
            messages.info(request,'username or password is incorrect, please try again or contact the adminstrator')

    context={}
    return render(request,'generalUsers/login.html',context) #renders the login page

def registerPage(request):
    regForm = CreateUserForm()
    #store data into the databse
    if request.method=="POST":
        regForm= CreateUserForm(request.POST)
        #check if the form is valid before saving to the database
        if regForm.is_valid():
            regForm.save() #save details to the database
            #get first and last name of user registered
            firstName = regForm.cleaned_data.get('first_name')
            lastName = regForm.cleaned_data.get('last_name')
            name = firstName +' '+lastName

            #pass messages to the dashboard
            messages.success(request,name+' has successfully been registered and is able to login.')

            return redirect('loginUser') #redirects user to the login page for the user to login
    context = {'form':regForm}
    return render(request,'generalUsers/register.html',context)#renders the register page with context details 

#logout user from the system
def logoutUser(request):
    logout(request)
    return redirect('loginUser')


#restrict the police user dashboard
@login_required(login_url='loginUser')
def userDash(request):
    return render(request,'generalUsers/dashboard.html')

def index(request):
    return render(request,'index.html')

#Method to genrate OTP with a timer
def generatedOTP():
  #generated 6 digit OTP
  print("Your OTP is:",totp.now())

