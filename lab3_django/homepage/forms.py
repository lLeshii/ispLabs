from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="UserEmail", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(label="UserEmail", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

