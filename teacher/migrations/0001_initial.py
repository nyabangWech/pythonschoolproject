# Generated by Django 5.0.6 on 2024-06-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('Nationality', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=6)),
                ('level_of_education', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('id_number', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]
