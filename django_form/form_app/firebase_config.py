import pyrebase

config={
  "apiKey": "AIzaSyCZeHCxhOtuAeyY3AGqjaZ3bnqWChWtr-A",
  "authDomain": "django-form-ea8fd.firebaseapp.com",
  "projectId": "django-form-ea8fd",
  "storageBucket": "django-form-ea8fd.firebasestorage.app",
  "messagingSenderId": "121406994261",
  "appId": "1:121406994261:web:fcf65b7a1e47474c2421dc",
  "databaseURL":"https://django-form-ea8fd-default-rtdb.asia-southeast1.firebasedatabase.app/",
}

firebase=pyrebase.initialize_app(config)
authenticate=firebase.auth()
db=firebase.database()
