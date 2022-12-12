from django.urls import path

# Import varibales from views.py
from .import views

# Define URI for generalUser apps
urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.userDash,name="userDash"),
    path('register',views.registerPage,name="registerUser"),
    path('login',views.loginPage,name="loginUser"),
    path('logout',views.logoutUser,name="logoutUser"),
]
