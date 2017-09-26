from django import forms
from django.contrib.auth.models import User


# from .fields import PasswordField


class CreateUser(forms.Form):
    #     username = forms.CharField(max_length=150)
    #     password = forms.CharField

    # class UserCreationForm(forms.ModelForm):

    error_messages = {
        'username': 'A user with that username already exists.',
        'password_mismatch': 'The two password fields didn\'t match.',
    }

    username = forms.CharField(max_length=150)
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Password Confirmation',
                                help_text='Enter the same password as above, for verification.')

    def clean_username(self):
        username = self.cleaned_data['username']
        result = User.objects.filter(username=username)
        if len(result) > 0:
            raise forms.ValidationError(
                self.error_messages['username'],
                code='username',
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
