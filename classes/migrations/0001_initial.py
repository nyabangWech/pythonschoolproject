# Generated by Django 5.0.6 on 2024-06-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_seat', models.IntegerField()),
                ('number_of_students', models.IntegerField()),
                ('class_name', models.CharField(max_length=20)),
                ('name_of_teachers', models.CharField(max_length=30)),
            ],
        ),
    ]
