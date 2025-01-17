from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label="Email"
    )
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        # help_text='150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.'
    )
    email = forms.EmailField(
        max_length=255,
       
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
