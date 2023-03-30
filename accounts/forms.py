from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    username = forms.CharField(max_length=254, required=True, help_text='Required. Enter a valid username.')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True,
                                help_text='Required. Enter a valid password.')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required. Enter the same '
                                                                                     'password as before.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
