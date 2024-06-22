# authentication/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication.models import BaseUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = BaseUser
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    class Meta:
        model = BaseUser
        fields = ['name', 'email', 'password1', 'password2']
