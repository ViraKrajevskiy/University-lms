from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Region, Department, Employ
from .forms import RegionForm, DepartmentForm, EmployForm


def index(request):
    region = Region.object.all()
    departament = Department.object.all()
    eployee = Employ.object.all()

    context={
        "region":region,
        "departament":departament,
        "eployee":eployee,
    }
    return render(request,'index.html',context=context)



class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html'
    context_object_name = 'regions'

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'region_form.html'
    success_url = reverse_lazy('region_list')

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'region_form.html'
    success_url = reverse_lazy('region_list')

class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('region_list')


class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department_form.html'
    success_url = reverse_lazy('department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department_form.html'
    success_url = reverse_lazy('department_list')

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('department_list')



class EmployListView(ListView):
    model = Employ
    template_name = 'employ_list.html'
    context_object_name = 'employees'

class EmployCreateView(CreateView):
    model = Employ
    form_class = EmployForm
    template_name = 'employ_form.html'
    success_url = reverse_lazy('employ_list')

class EmployUpdateView(UpdateView):
    model = Employ
    form_class = EmployForm
    template_name = 'employ_form.html'
    success_url = reverse_lazy('employ_list')

class EmployDeleteView(DeleteView):
    model = Employ
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('employ_list')
