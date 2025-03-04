from django.urls import path
from .views import fan_create, student_create, student_pdf

urlpatterns = [
    path('fan/create/', fan_create, name='fan_create'),
    path('student/create/', student_create, name='student_create'),
    path('student/<int:student_id>/pdf/', student_pdf, name='student_pdf'),
]
