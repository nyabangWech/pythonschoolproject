# Generated by Django 5.0.7 on 2024-08-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_alter_classes_school_year'),
        ('course', '0003_rename_number_of_courses_course_id_of_course_and_more'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(related_name='student', to='classes.classes'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='student', to='course.course'),
        ),
    ]
