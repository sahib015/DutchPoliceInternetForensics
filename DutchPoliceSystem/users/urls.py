from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name="index"),
    path('register',views.index,name="register"), #to change to load the registration form
    path('login',views.index,name="login"), #to change to load the login form
    path('profile',views.index,name="profile"),# to change to load the profile view
    path('logout',views.index,name="logout"),# to change the logout
]