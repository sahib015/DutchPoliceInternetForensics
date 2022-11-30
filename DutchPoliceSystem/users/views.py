from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):
    return render(request,'users/login.html')

def registerPage(request):
    regForm = UserCreationForm()
    #store data into the databse
    if request.method=="POST":
        regForm= UserCreationForm(request.POST)
        #check if the form is valid before saving to the database
        if regForm.is_valid():
            regForm.save() #save details to the database
    context = {'form':regForm}
    return render(request,'users/register.html',context)
