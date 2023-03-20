from .models import Employee
from django.db.models.signals import post_save
from django.dispatch import receiver
import firebase_admin
from firebase_admin import db
import os


@receiver(post_save, sender=Employee)
def fun(sender, instance, **kwargs):
    data = os.path.abspath(os.path.dirname(__file__)) + "/key.json"

    cred_obj=firebase_admin.credentials.Certificate(data)
    databaseURL="https://rtmdb-b6919-default-rtdb.firebaseio.com/"
    default_app = firebase_admin.initialize_app(cred_obj,{'databaseURL':databaseURL})
    
    data = {
        "empid":instance.empid,
        "name":instance.name,
        "city":instance.city
    }
    
    ref= db.reference(f'{instance.name}')
    ref.set(data)