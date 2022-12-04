from django.forms import ModelForm
from django import forms
from .models import UploadDataModel

class UploadDataForm(forms.ModelForm):
    class Meta:
        model = UploadDataModel
        fields = ('first_name', 'last_name', 'email', 'title', 'file', 'desc')
