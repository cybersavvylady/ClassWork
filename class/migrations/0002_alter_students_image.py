# Generated by Django 4.2.6 on 2023-10-30 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(default='uploads/images/profile.jpg', upload_to='uploads/images'),
        ),
    ]