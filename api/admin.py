from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmpAd(admin.ModelAdmin):
    list_display=['name','empid','city']