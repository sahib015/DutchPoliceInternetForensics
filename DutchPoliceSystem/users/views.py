#required imports
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateRegistrationForm

# Create your views here.

def loginPage(request):
    return render(request,'users/login.html')

def registerPage(request):
    regForm = CreateRegistrationForm()
    #store data into the databse
    if request.method=="POST":
        regForm= CreateRegistrationForm(request.POST)
        #check if the form is valid before saving to the database
        if regForm.is_valid():
            regForm.save() #save details to the database
            #get first and last name of user registered
            firstName = regForm.cleaned_data.get('first_name')
            lastName = regForm.cleaned_data.get('last_name')
            name = firstName +' '+lastName

            #pass messages to the dashboard
            messages.success(request,name+' has successfully been registered and is able to login.')

            return redirect('login') #redirects user to the admin dashboard (to be done later)- temporary redirection to login page
    context = {'form':regForm}
    return render(request,'users/register.html',context)
