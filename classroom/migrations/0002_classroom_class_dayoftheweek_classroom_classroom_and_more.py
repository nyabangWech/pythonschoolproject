# Generated by Django 5.0.7 on 2024-07-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='class_dayoftheweek',
            field=models.CharField(default='Monday', max_length=20),
        ),
        migrations.AddField(
            model_name='classroom',
            name='classroom',
            field=models.CharField(default='7:00', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classroom',
            name='new_classroom',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
