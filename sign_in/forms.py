from django import forms
from . import models


class signup(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = ['username', 'password']


class signin(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = ['username', 'password']



