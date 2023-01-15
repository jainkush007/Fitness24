from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # contact = forms.CharField(label = "Phone No.",max_length=10)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    contact = forms.CharField(label="Phone No.", max_length=10)
    First_Name = forms.CharField(label="First Name")
    Last_Name = forms.CharField(label="Last Name")
    DOB = forms.CharField(label="DOB (DD/MM/YYYY)",max_length=10,min_length=10)
    City = forms.CharField(label="City")
    State = forms.CharField(label="State")
    Pincode = forms.IntegerField(label="Pincode")
    class Meta:
        model = Profile
        fields = [
                    'First_Name',
                    'Last_Name',
                    'contact',
                    'DOB',
                    'City',
                    'State',
                    'Pincode',
                    'image'
                 ]