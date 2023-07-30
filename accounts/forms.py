from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from chat.models import Account


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'avatar']