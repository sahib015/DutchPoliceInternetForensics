from django.urls import path

# Import varibales from views.py
from . import views

# Import varibales from other apps
from userNotifications.views import allUserList

# Define URI for policeUsers apps
urlpatterns = [
    path('',views.home,name="policeDash"),
    path('register',views.registerPage,name="registerPolice"),
    path('login',views.loginPage,name="login"),
    path('profile',views.loginPage,name="profile"),
    path('logout',views.logoutUser,name="logout"),
    path('allMessages',allUserList,name="allMessages"),
]
