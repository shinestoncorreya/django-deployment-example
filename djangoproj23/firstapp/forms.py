from django.forms import ModelForm
from django.contrib.auth.models import User
from firstapp import models
from django import forms

class UserProfile_form(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=('username', 'password', 'email')

class UserAdditional_form(ModelForm):
    class Meta:
        model=models.UserProfile
        fields=('portfolio', 'profile_pic')
