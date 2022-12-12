#required imports
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Import variables from forms.py
from .forms import CreateUserForm

#OTP Import
import pyotp

#variables declared to be used publicly

totp = pyotp.TOTP('base32secret3232')
# Create your views here.

# General User Login Page Function
def loginPage(request):

    if request.method =="POST":
        #get username and password values from the login form
        usernameVal = request.POST.get('usernameUser')
        passwordVal = request.POST.get('passwordUser')

         #authenticate user
        user =authenticate(request,username=usernameVal,password=passwordVal)

        #check if user is in the databse
        if user is not None:

            #Generator OTP passcode
            generatedOTP()

            #verify generated OTP that has been generated
           
            verifyOTP= input("Enter OTP: ")
            if totp.verify(verifyOTP)==True:
                login(request,user)
                return redirect('userDash') # redirects to the User Dashboard after sucesssful OTP Verification
            else:
                messages.warning(request,'Verification of OTP failed.')
                print("invalid OTP")

        else:
            messages.info(request,'username or password is incorrect, please try again or contact the adminstrator')

    context={}
    #renders the login page
    return render(request,'generalUsers/login.html',context)

# General User Registration Page
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

            #redirects user to the login page for the user to login
            return redirect('loginUser')
    context = {'form':regForm}

    ##renders the register page with context details
    return render(request,'generalUsers/register.html',context)

#logout user from the system
def logoutUser(request):
    logout(request)
    return redirect('index')


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
