# Generated by Django 4.0.5 on 2023-08-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='DEFAULT VALUE', max_length=255),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='DEFAULT VALUE', max_length=255),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='DEFAULT VALUE', max_length=255),
        ),
    ]