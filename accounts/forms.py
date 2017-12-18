from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactAppUser(UserCreationForm):
    username = forms.CharField(max_length=200, required=True, label='Username')
    first_name = forms.CharField(max_length=200, required=True, label='First Name')
    last_name = forms.CharField(max_length=200, required=True, label='Last Name')
    email = forms.CharField(max_length=500, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(max_length=500, required=True, widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(max_length=500, required=True, widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        )
