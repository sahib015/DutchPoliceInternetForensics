from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.userDash,name="userDash"),
    path('register',views.registerPage,name="registerUser"),
    path('login',views.loginPage,name="loginUser"),
    path('profile',views.loginPage,name="profile"),
    path('logout',views.logoutUser,name="logoutUser"),
]