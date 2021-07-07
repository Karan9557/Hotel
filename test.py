import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAZCZ7w8eonEdPFsrprbWU3_c1lyxQgGjg",
    'authDomain': "hotel-56011.firebaseapp.com",
    'databaseURL': "https://hotel-56011-default-rtdb.firebaseio.com/",
    'projectId': "hotel-56011",
    'storageBucket': "hotel-56011.appspot.com",
    'messagingSenderId': "617940653545",
    'appId': "1:617940653545:web:6e4bc4a483e3bbc742a778",
    'measurementId': "G-40RPQJZMY3"

  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#db.child('users').set({'abc':'dfd'})
db.child('users').push({'xyz':'dfs'})