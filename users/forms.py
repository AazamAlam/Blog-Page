from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#creating a new form with an extra field, inheriting the UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()# default = true

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    #Meta creates and holds the configuration of the form, model is the thing that is getting affect
    # new user is being creatted, and the fields indicate which order each form field should pop up