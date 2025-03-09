from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, FileResponse, HttpResponseForbidden, Http404
from django.urls.base import reverse_lazy

from configapp.forms import *
import qrcode
import os
from io import BytesIO
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from .models import *
from django.views.generic import *

def generate_student_pdf(student):
    """Создаёт PDF с данными указанного студента."""
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=A4)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Info about student")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 760, f"Name: {student.full_name}")
    pdf.drawString(100, 740, f"Phone number: {student.phone_number}")
    pdf.drawString(100, 720, f"Adress: {student.address}")
    pdf.drawString(100, 700, f"Subject: {student.fan.title}")
    pdf.drawString(100, 680, f"Teacher: {student.teacher.teacherName}")

    # Добавление фото (если есть)
    if student.photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, str(student.photo))
        if os.path.exists(photo_path):
            pdf.drawImage(ImageReader(photo_path), 100, 550, width=100, height=100)

    pdf.showPage()
    pdf.save()

    pdf_buffer.seek(0)  # Важно, чтобы PDF не был пустым
    return pdf_buffer


def download_student_pdf(request, student_id):
    """Позволяет скачать данные любого студента по его ID."""
    student = get_object_or_404(Student, id=student_id)

    # Генерируем PDF
    pdf_buffer = generate_student_pdf(student)

    if not pdf_buffer:  # Проверяем, чтобы не было None
        raise Http404("Ошибка при создании PDF")

    # Отправляем файл пользователю
    return FileResponse(pdf_buffer, as_attachment=True, filename=f"{student.full_name}.pdf")





def index(request):
    fans = Fan.objects.all()
    students = Student.objects.all()

    context = {
        "fans":fans,
        "students":students
    }
    return render(request,'index.html',context=context)

def AboutStudent(request, new_id):
    studentses = Student.objects.get(pk=new_id)
    fanse = Fan.objects.all()

    context = {
        "new":studentses,
        "fanse":fanse,
    }
    return render(request, 'fan_form.html', context=context)

def filtering(request, fan_id):
    students = Student.objects.filter(fan__id=fan_id)  # Используем fan__id вместо fan_id
    fans = Fan.objects.all()

    context = {
        "students": students,
        "fans": fans,
    }
    return render(request, 'Filter_student.html', context=context)
    

# def teachercreate(request):
#     if request.method == 'POST':
#         form = TeacherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = TeacherForm()
#     return render(request, 'teacherad.html', {'form': form})



def generate_qr(request):
    # Ссылка на Telegram-канал
    telegram_link = "https://t.me/c/1326340751/1214"

    # Создание QR-кода
    qr = qrcode.make(telegram_link)

    # Сохранение QR-кода в памяти
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    # Возвращаем изображение как HTTP-ответ
    return HttpResponse(buffer.getvalue(), content_type="image/png")


#
# def fan_create(request):
#     if request.method == 'POST':
#         form = FanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = FanForm()
#     return render(request, 'fan_form.html', {'form': form})
#
# def student_create(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = StudentForm()
#     return render(request, 'student_form.html', {'form': form})
#
# # Обновление
# def update_teacher(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id)
#     if request.method == "POST":
#         form = TeacherForm(request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_list')  # Измени на свой маршрут
#     else:
#         form = TeacherForm(instance=teacher)
#     return render(request, 'about_teacher.html', {'form': form})
#
#
# def update_fan(request, fan_id):
#     fan = get_object_or_404(Fan, id=fan_id)
#     if request.method == "POST":
#         form = FanForm(request.POST, instance=fan)
#         if form.is_valid():
#             form.save()
#             return redirect('fan_list')  # Измени на свой маршрут
#     else:
#         form = FanForm(instance=fan)
#     return render(request, 'about_fan.html', {'form': form})
#
#
# def update_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     if request.method == "POST":
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')  # Измени на свой маршрут
#     else:
#         form = StudentForm(instance=student)
#     return render(request, 'about_student.html', {'form': form})
#
#
# # Удаление учителя
# def delete_teacher(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id)
#     if request.method == "POST":
#         teacher.delete()
#         return redirect('teacher_list')  # Измени на свой маршрут
#     return render(request, 'delete_all.html', {'object': teacher, 'type': 'учителя'})
#
# def delete_fan(request, fan_id):
#     fan = get_object_or_404(Fan, id=fan_id)
#     if request.method == "POST":
#         fan.delete()
#         return redirect('fan_list')  # Измени на свой маршрут
#     return render(request, 'delete_all.html', {'object': fan, 'type': 'предмета'})
#
#
# def delete_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     if request.method == "POST":
#         student.delete()
#         return redirect('student_list')  # Измени на свой маршрут
#     return render(request, 'delete_all.html', {'object': student, 'type': 'студента'})
#
#
#
class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacherad.html'
    success_url = reverse_lazy('home')

class FanCreateView(CreateView):
    model = Fan
    form_class = FanForm
    template_name = 'fan_form.html'
    success_url = reverse_lazy('home')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'about_student.html'
    success_url = reverse_lazy('home')

# Обновление
class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'about_teacher.html'
    success_url = reverse_lazy('teacher_list')

class FanUpdateView(UpdateView):
    model = Fan
    form_class = FanForm
    template_name = 'about_fan.html'
    success_url = reverse_lazy('fan_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'about_student.html'
    success_url = reverse_lazy('student_list')

# Удаление
class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'delete_all.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'учителя'
        return context

class FanDeleteView(DeleteView):
    model = Fan
    template_name = 'delete_all.html'
    success_url = reverse_lazy('fan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'предмета'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_all.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'студента'
        return context
