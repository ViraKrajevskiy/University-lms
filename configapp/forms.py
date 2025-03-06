from django import forms
from .models import *
import re

class TeahcerForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacherName']
        widgets = {
            'teacherName':forms.TextInput(attrs={'class':'form-control'}),
        }

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['title']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_title(self):
        title = self.changed_data['title']
        if re.match(r'\d',title):
            raise ValueError('The name space is not started to number')
        return title

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'address', 'fan','teacher']
        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control','rows':5}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'fan':forms.Select(attrs={'class':'form-control'}),
            'teacher':forms.Select(attrs={'class':'form-control'}),
        }
