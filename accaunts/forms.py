from django import forms

from page.models import CustomUser


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=20)


class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username',
                'first_name',
                'last_name',
                'password']

