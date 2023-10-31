from django.db import models


# Create your models here.

# classes: structure/how something appears/the design/blueprint

# models represent tables in the DB

class Students(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to="uploads/images", default='uploads/images/profile.jpg')

    def __str__(self):
        return self.name

# any minute you modify the models file, YOU MUST make and run migrations

# python manage.py makemigrations: create table(model) in the database

# python manage.py migrate:updates the table/model

