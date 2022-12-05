from django.urls import path
from .import views
from userNotifications.views import allUserList
urlpatterns = [
    path('',views.home,name="policeDash"),
    path('register',views.registerPage,name="register"),
    path('login',views.loginPage,name="login"),
    path('profile',views.loginPage,name="profile"),
    path('logout',views.logoutUser,name="logout"),
    path('allMessages',allUserList,name="allMessages"),
]