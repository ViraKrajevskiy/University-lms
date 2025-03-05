from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('fan/create/', fan_create, name='fan_create'),
    path('student/create/', student_create, name='student_create'),
    path('student/<int:student_id>/pdf/', student_pdf, name='student_pdf'),
    path('filter/<int:fan_id>',filter,name='filter'),
    # path('delete_student/<int:student_id>/', delete_student, name='delete_student'),    
]
