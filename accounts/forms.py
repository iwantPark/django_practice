from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
            max_length=255, 
            help_text='Enter a valid email address'
            )
    nickname = forms.CharField(
            max_length=255, 
            help_text='Enter a valid nickname',
            required=True
            )
    password1 = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(),
            help_text='Your password must contain at least 8 characters.',
            )
    password2 = forms.CharField(
            label='Password confirmation',
            widget=forms.PasswordInput(),
            help_text='Enter the same password as before, for verification.',
            )
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']