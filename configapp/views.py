from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, FileResponse
from configapp.forms import *
from reportlab.pdfgen import canvas
from io import BytesIO
import qrcode
import os
from django.conf import settings


def generate_student_pdf(student):
    pdf_dir = os.path.join(settings.MEDIA_ROOT, 'pdf')
    os.makedirs(pdf_dir, exist_ok=True)  # Создаём папку, если её нет

    pdf_path = os.path.join(pdf_dir, f"{student.full_name}.pdf")

    # Создаём PDF
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Информация о студенте")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 760, f"ФИО: {student.full_name}")
    pdf.drawString(100, 740, f"Телефон: {student.phone_number}")
    pdf.drawString(100, 720, f"Адрес: {student.adress}")
    pdf.drawString(100, 700, f"Предмет: {student.fan}")
    pdf.drawString(100, 680, f"Учитель: {student.teacher}")
    pdf.drawImage(100,700,f"Фото: {student.photo}")

    pdf.showPage()
    pdf.save()

    with open(pdf_path, "wb") as f:
        f.write(pdf_buffer.getvalue())

    return pdf_path


def download_student_pdf(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    pdf_path = generate_student_pdf(student)

    return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename=f"{student.full_name}.pdf")

def index(request):
    fans = Fan.objects.all()
    students = Student.objects.all()

    context = {
        "fans":fans,
        "students":students
    }
    return render(request,'index.html',context=context)

def AboutStudent(request,id):
    students = Student.objects.get(pk=id)

    context = {
        "student":students,
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
    



def teachercreate(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'teacherad.html', {'form': form})



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



def fan_create(request):
    if request.method == 'POST':
        form = FanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FanForm()
    return render(request, 'fan_form.html', {'form': form})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Обновление
def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # Измени на свой маршрут
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'about_teacher.html', {'form': form})


def update_fan(request, fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    if request.method == "POST":
        form = FanForm(request.POST, instance=fan)
        if form.is_valid():
            form.save()
            return redirect('fan_list')  # Измени на свой маршрут
    else:
        form = FanForm(instance=fan)
    return render(request, 'about_fan.html', {'form': form})


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Измени на свой маршрут
    else:
        form = StudentForm(instance=student)
    return render(request, 'about_student.html', {'form': form})


# Удаление учителя
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_list')  # Измени на свой маршрут
    return render(request, 'delete_all.html', {'object': teacher, 'type': 'учителя'})

def delete_fan(request, fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    if request.method == "POST":
        fan.delete()
        return redirect('fan_list')  # Измени на свой маршрут
    return render(request, 'delete_all.html', {'object': fan, 'type': 'предмета'})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')  # Измени на свой маршрут
    return render(request, 'delete_all.html', {'object': student, 'type': 'студента'})



