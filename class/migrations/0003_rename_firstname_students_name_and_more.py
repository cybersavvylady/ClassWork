# Generated by Django 4.2.6 on 2023-10-31 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_alter_students_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='lastname',
        ),
    ]
