from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from configapp.forms import *
from io import BytesIO
from reportlab.pdfgen import canvas

def index(request):
    fans = Fan.objects.all()
    students = Student.objects.all()

    context = {
        "fans":fans,
        "students":students
    }
    return render(request,'index.html',context=context)

def filtering(request,fan_id):
    students = Student.objects.filter(fan_id=fan_id)
    fans = Fan.objects.all()

    context = {
        "students":students,
        "fans":fans,
    }
    return render(request, 'Filter_student.html', context=context)

def teachercreate(request):
    if request.method == 'POST':
        form = TeahcerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeahcerForm()
    return render(request, 'teacherad.html', {'form': form})





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
        form = TeahcerForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # Измени на свой маршрут
    else:
        form = TeahcerForm(instance=teacher)
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



