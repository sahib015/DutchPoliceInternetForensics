from django.urls import path
from . import views

# Define URI for userNotifications apps
urlpatterns = [
    path('addMessage', views.createMessage,name="addMessage"),
]
