from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import FullDetail
from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmpassword = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','password','confirmpassword','email']
#EXTRA INFO
class InfoProfileForm(forms.ModelForm):
    class Meta:
        model = FullDetail
        fields = ['address']

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
