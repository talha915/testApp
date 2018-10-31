from django.db import models
from django.core.validators import  MinValueValidator
# Create your models here.
class Student(models.Model):
    std_name = models.CharField(max_length=30)
    std_address = models.CharField(max_length=250)
    std_age = models.IntegerField(validators = [
            MinValueValidator(1)
        ]
    )

class Students(models.Model):
    std_name = models.CharField(max_length=30)
    std_address = models.CharField(max_length=250)
    std_age = models.IntegerField(validators = [
            MinValueValidator(1)
        ]
    )