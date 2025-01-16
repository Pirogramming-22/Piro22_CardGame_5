from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        help_text='150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        help_text='최소 8자 이상의 비밀번호를 입력하십시오'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        help_text='같은 비밀번호를 한번 더 입력하십시오'
    )

    class Meta:
        model = get_user_model()  # Ensure it uses the custom user model.
        fields = ('username', 'password1', 'password2')