from django import forms
from django.contrib.auth import get_user_model

from profiles.models import Message


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['last_name', 'first_name', 'date_birth', 'photo']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='User')
    password1 = forms.CharField(label='pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label='pass again', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'body']