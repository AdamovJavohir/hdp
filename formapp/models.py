from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
