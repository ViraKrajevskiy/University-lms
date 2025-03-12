from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *
import re


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields= ('username','password')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacherName']
        widgets = {
            'teacherName': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_teacherName(self):
        teacher_name = self.cleaned_data.get('teacherName')
        if not teacher_name.isalpha():
            raise forms.ValidationError("Teacher name should contain only letters.")
        return teacher_name


class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if re.match(r'\d', title):
            raise forms.ValidationError("The name cannot start with a number.")
        return title


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'address', 'fan', 'teacher', 'photo']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'fan': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not all(x.isalpha() or x.isspace() for x in full_name):
            raise forms.ValidationError("Full name should only contain letters and spaces.")
        return full_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.fullmatch(r'^\d{9,15}$', str(phone_number)):
            raise forms.ValidationError("Phone number should be between 9 and 15 digits.")
        return phone_number

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 5:
            raise forms.ValidationError("Address must be at least 5 characters long.")
        return address
        