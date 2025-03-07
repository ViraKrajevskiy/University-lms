from django.db import models

class Teacher(models.Model):
    teacherName = models.CharField(max_length=60)  # Исправлено

    def __str__(self):
        return self.teacherName  # Добавлен метод __str__

class Fan(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)  # Связь с Fan
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Связь с Teacher
    photo = models.ImageField(upload_to='students_photos/', blank=True, null=True)
    



    def __str__(self):
        return self.full_name
        