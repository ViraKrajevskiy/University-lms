from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
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

def filter(request,fan_id):
    students = Student.objects.filter(fan_id=fan_id)
    fans = Fan.objects.all()


    context = {
        "fans":fans,
        "students":students
    }
    return render(request,'fan_info.html',context=context)


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

def student_pdf(request, student_id):
    student = Student.objects.get(id=student_id)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, f"Student: {student.full_name}")
    p.drawString(100, 780, f"Telefon: {student.phone_number}")
    p.drawString(100, 760, f"Manzil: {student.address}")
    p.drawString(100, 740, f"Fan: {student.fan.title}")
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
    

def delete_student(request, student_id):
    new = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = FanForm(request.POST,isinstance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = FanForm(instance= new)
        return redirect(request,'students_list')  # Замени на свой URL списка



def update_new(request, new_id):
    new = get_object_or_404(Student, id = new_id)
    context = {
        "new":new
    }
    return render(request,'about_student.html',context)


