# Generated by Django 5.1.6 on 2025-03-08 15:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('phone', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Введите корректный номер', regex='^\\+?[0-9]{10,15}$')])),
                ('data_file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('fk_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Region.department')),
                ('fk_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Region.region')),
            ],
        ),
    ]
