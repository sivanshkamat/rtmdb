import firebase_admin
from firebase_admin import credentials, auth, db
import os
from django.shortcuts import render
import firebase

firebaseConfig = {
  "apiKey": "AIzaSyCouEGy6HZubeasoDK-kT0VXADScG129XM",
  "authDomain": "rtmdb-b6919.firebaseapp.com",
  "projectId": "rtmdb-b6919",
  "storageBucket": "rtmdb-b6919.appspot.com",
  "databaseURL":"https://console.firebase.google.com/u/0/project/rtmdb-b6919/database/rtmdb-b6919-default-rtdb/data/~2F",
  "messagingSenderId": "322781684128",
  "appId": "1:322781684128:web:ca8406da023f301856c4c5",
  "measurementId": "G-MB18G4WJ5G"
};
if not firebase_admin._apps:
  data = os.path.abspath(os.path.dirname(__file__)) + "/key.json"
  cred = credentials.Certificate(data)
  firebase_admin.initialize_app(cred)
  ref = db.reference('server/saving-data/fireblog')
  # auth=firebase_admin.auth()

  users_ref = ref.child('Employee')
  users_ref.set({
      'sivansh': {
          'city': 'Biratnagar',
          'empid': '101903808'
      }
  })