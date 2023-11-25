from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import profileModel


def validate_characters(value):
    if not value.isalpha():
        raise forms.ValidationError('Only characters are allowed.')


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(validators=[validate_characters])
    last_name = forms.CharField(validators=[validate_characters])
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['first_name', 'last_name', 'email',
                          'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profileModel
        fields = ['image']
