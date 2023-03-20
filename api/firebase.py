import firebase_admin
import json
from firebase_admin import credentials, auth, db
import os
from django.shortcuts import render
# import firebase
data = os.path.abspath(os.path.dirname(__file__)) + "/key.json"
details = os.path.abspath(os.path.dirname(__file__)) + "/details.json"
cred_obj=firebase_admin.credentials.Certificate(data)
databaseURL="https://rtmdb-b6919-default-rtdb.firebaseio.com/"
default_app = firebase_admin.initialize_app(cred_obj,{'databaseURL':databaseURL})

ref= db.reference("/")

with open(details,"r") as f:
  file_contents = json.load(f)
ref.set(file_contents)