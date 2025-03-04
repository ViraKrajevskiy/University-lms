from django.db import models

class Fan(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
        