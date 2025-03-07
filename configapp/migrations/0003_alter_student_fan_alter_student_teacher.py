# Generated by Django 5.1.6 on 2025-03-06 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0002_student_photo_alter_student_fan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.fan'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.teacher'),
        ),
    ]
