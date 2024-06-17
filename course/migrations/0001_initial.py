# Generated by Django 5.0.6 on 2024-06-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_course', models.CharField(max_length=20)),
                ('duration_of_course', models.DateField()),
                ('number_of_students', models.IntegerField(max_length=20)),
                ('number_of_courses', models.IntegerField()),
                ('name_of_teachers', models.CharField(max_length=30)),
            ],
        ),
    ]
