from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta(UserCreationForm.Meta):
        User = get_user_model()
        model = User
        fields = ["username", "email", "password1", "password2"]
