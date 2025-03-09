from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Region(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Employ(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(regex=r'^\+?[0-9]{10,15}$', message="Введите корректный номер")]
    )
    data_file = models.FileField(upload_to='uploads/', blank=True, null=True)

    fk_dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    fk_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
