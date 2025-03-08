from django.urls import path
from .views import *


urlpatterns = [
    path('download_student/<int:student_id>/', download_student_pdf, name='download_student_pdf'),

    path('qr/', generate_qr, name='generate_qr'),

    path('',index,name='home'),
    path('filtering/<int:fan_id>', filtering, name='filtering'),
    path('new/<int:new_id>',AboutStudent,name='AboutStudent'),

    # Создание
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('fan/create/', FanCreateView.as_view(), name='fan_create'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),

    # Обновление
    path('teacher/update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('fan/update/<int:pk>/', FanUpdateView.as_view(), name='fan_update'),
    path('student/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),

    # Удаление
    path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete'),
    path('fan/delete/<int:pk>/', FanDeleteView.as_view(), name='fan_delete'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]

