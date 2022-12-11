from django.urls import path
from . import views

urlpatterns = [
    path('addMessage', views.createMessage,name="addMessage"),
]
