from django import forms

class LoginForm(forms.Form):
    """
    Login form - presented to the user to enter their details. Will be used to authenticate the users against the database.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)