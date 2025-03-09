from django import forms
from .models import Region, Department, Employ

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название региона'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название отдела'}),
        }

class EmployForm(forms.ModelForm):
    class Meta:
        model = Employ
        fields = ['last_name', 'first_name', 'middle_name', 'email', 'phone', 'data_file', 'fk_dep', 'fk_region']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'data_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'fk_dep': forms.Select(attrs={'class': 'form-control'}),
            'fk_region': forms.Select(attrs={'class': 'form-control'}),
        }
        