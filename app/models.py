from django.db import models

# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
