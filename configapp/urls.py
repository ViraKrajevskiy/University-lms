from django.contrib.admindocs.utils import named_group_matcher
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('filtering/<int:fan_id>', filtering, name='filtering'),

    path('teacherad/create/',teachercreate,name = 'teacheradd'),
    path('teacher/update/<int:teacher_id>/', update_teacher, name='update_teacher'),
    path('teacher/delete/<int:teacher_id>/', delete_teacher, name='delete_teacher'),

    path('fan/create/', fan_create, name='fan_create'),
    path('fan/update/<int:fan_id>/', update_fan, name='update_fan'),
    path('fan/delete/<int:fan_id>/', delete_fan, name='delete_fan'),

    path('student/create/', student_create, name='student_create'),
    path('student/update/<int:student_id>/', update_student, name='update_student'),
    path('student/delete/<int:student_id>/', delete_student, name='delete_student'),
]
