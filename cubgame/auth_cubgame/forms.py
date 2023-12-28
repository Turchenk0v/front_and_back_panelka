from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=60)
    password = forms.CharField(widget=forms.PasswordInput())
    check_password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=60)
    password = forms.CharField(widget=forms.PasswordInput())
