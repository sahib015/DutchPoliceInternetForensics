from django import forms

# Import variables from models.py
from .models import UploadDataModel,CreateNewMessage

# Define upload form fields class
class UploadDataForm(forms.ModelForm):
    class Meta:
        model = UploadDataModel
        fields = ('first_name', 'last_name', 'email', 'title', 'file', 'description')

# Define new message form fields class
class CreateNewMessageFrom(forms.ModelForm):
    class Meta:
        model = CreateNewMessage
        fields =('date','name','email','content','levelOfPriority')
