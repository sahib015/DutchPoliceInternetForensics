
from django.forms import ModelForm
from django import forms
from .models import UploadDataModel,CreateNewMessage




class UploadDataForm(forms.ModelForm):
    class Meta:
        model = UploadDataModel
        fields = ('first_name', 'last_name', 'email', 'title', 'file', 'description')

class CreateNewMessageFrom(forms.ModelForm):
    class Meta:
        model = CreateNewMessage
        fields =('date','name','email','content','levelOfPriority')
        