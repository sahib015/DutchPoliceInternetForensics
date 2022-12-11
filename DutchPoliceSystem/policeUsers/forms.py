from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User Creation Form Class
class CreateRegistrationForm(UserCreationForm):
    class Meta:
        model = User

        # Define fields for  the user registration form
        fields =['username','first_name','last_name','email','password1','password2']
