# Generated by Django 5.0.7 on 2024-08-01 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_course_prestiquies_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='number_of_courses',
            new_name='ID_of_course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name_of_teachers',
            new_name='name_of_teacher',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='duration_of_course',
            new_name='startyear_of_course',
        ),
    ]