from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index,name='home'),

    path('regions/', RegionListView.as_view(), name='region_list'),
    path('regions/create/', RegionCreateView.as_view(), name='region_create'),
    path('regions/update/<int:pk>/', RegionUpdateView.as_view(), name='region_update'),
    path('regions/delete/<int:pk>/', RegionDeleteView.as_view(), name='region_delete'),

    # Department
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'),

    # Employ
    path('employees/', EmployListView.as_view(), name='employ_list'),
    path('employees/create/', EmployCreateView.as_view(), name='employ_create'),
    path('employees/update/<int:pk>/', EmployUpdateView.as_view(), name='employ_update'),
    path('employees/delete/<int:pk>/', EmployDeleteView.as_view(), name='employ_delete'),

]