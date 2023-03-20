from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    empid=models.IntegerField()
    city=models.CharField(max_length=20)
    
    
