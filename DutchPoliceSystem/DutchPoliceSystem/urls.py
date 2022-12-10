"""DutchPoliceSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Define URI to be access
urlpatterns = [
    # Django Administrator portal URI
    path('admin/', admin.site.urls),
    # Internal User URI and reference with policeUsers.urls file in policeUsers directory
    path('government/',include('policeUsers.urls')),
    # Notification message URI and reference with userNotifications.urls file in userNotifications directory 
    path('', include('userNotifications.urls')),
    # General User URI and reference with generalUsers.urls file in generalUsers directory
    path('', include('generalUsers.urls'))
]
