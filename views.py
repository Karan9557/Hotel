from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase

tid = ''

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
auth = firebase.auth()

def home(HttpRequest):
    return HttpResponse('WELCOME')

def registration(HttpRequest):
    return render(HttpRequest,'registration.html')

#def design(HttpRequest):
    #return render(HttpRequest,'design.html')

def login(HttpRequest):
    return render(HttpRequest,'login.html')

def regi(HttpRequest):
    return render (HttpRequest,'regi.html')

def registrationdata(HttpRequest):
    fname = HttpRequest.POST.get('firstname')
    lname = HttpRequest.POST.get('lastname')
    kemail = HttpRequest.POST.get('email')
    fpass = HttpRequest.POST.get('password')
    dob = HttpRequest.POST.get('date')
    male = HttpRequest.POST.get('inlineRadioOptions')
    #female = HttpRequest.POST.get('inlineRadiOptions')
    add = HttpRequest.POST.get('address')
    ci = HttpRequest.POST.get('city')
    tate = HttpRequest.POST.get('state')

    print(fname)
    print(lname)
    print(kemail)
    print(male)
    print(fpass)
    print(tate)

    db.child('users').push({'firstname': fname,'lastname': lname,'email': kemail,'password': fpass,'radio':male,'state':tate})
    auth.create_user_with_email_and_password(kemail,fpass)

    return HttpResponse('Data Found')

def regidata(HttpRequest):
    fname = HttpRequest.POST.get('firstname')
    lname = HttpRequest.POST.get('lastname')
    kemail = HttpRequest.POST.get('Email')
    fpass = HttpRequest.POST.get('password')
    cpass =HttpRequest.POST.get('password')
    dob = HttpRequest.POST.get('date')
    male = HttpRequest.POST.get('inlineRadioOptions')
    ph = HttpRequest.POST.get('mobile')
    add = HttpRequest.POST.get('Address')
   # ci = HttpRequest.POST.get('city')
    tate = HttpRequest.POST.get('state')

    print(fname)
    print(lname)
    print(kemail)
    print(male)
    print(fpass)
    print(cpass)
    print(dob)
    print(ph)
    print(add)
    #print(ci)
    print(tate)

    db.child('users').push(
        {'firstname': fname, 'lastname': lname, 'Email': kemail, 'password': fpass, 'radio': male, 'state': tate})
    auth.create_user_with_email_and_password(kemail, fpass)

    return HttpResponse('Data Found')

def logindata(HttpRequest):
    mail = HttpRequest.POST.get('email')
    woed = HttpRequest.POST.get('password')

    print(mail)
    print(woed)

    auth.sign_in_with_email_and_password(mail,woed)

    return HttpResponse('you are logged in')

def test(HttpRequest):
    return  render(HttpRequest,'Reg.html')


def index(HttpRequest):
    return render (HttpRequest, 'index.html')

def form(HttpRequest):
    return render(HttpRequest, 'form.html')

def formdata(HttpRequest):
    cate = HttpRequest.POST.get('categary')
    name = HttpRequest.POST.get('fname')
    hotelname = HttpRequest.POST.get('Hname')
    price = HttpRequest.POST.get('RS')
    image = HttpRequest.POST.get('url')
   # City = HttpRequest.POST.get('city')
    text = HttpRequest.POST.get('abstract')

    print(cate)
    print(name)
    print(hotelname)
    print(price)
    print(image)
    #print(City)
    print(text)

    db.child('hotel').push(
      {'categary': cate, 'fname': name, 'Hname': hotelname, 'RS': price, 'files': image, 'abstract':text})
    #auth.create_user_with_email_and_password(kemail, fpass)


    return HttpResponse('Data Found')


def edit(HttpRequest):
    dt = db.child('hotel').shallow().get().val()
    print(dt)

    datalist = []

    for i in dt:
        print(i)
        datalist.append(i)
    datalist.sort(reverse=True)
    print(datalist)

    categary = []
    fname = []
    Hname = []
    RS = []
    files = []
    abstract = []

    for i in datalist:
        cat = db.child('hotel').child(i).child('categary').get().val()
        categary.append(cat)

        name = db.child('hotel').child(i).child('fname').get().val()
        fname.append(name)

        hotelname = db.child('hotel').child(i).child('Hname').get().val()
        Hname.append(hotelname)

        price = db.child('hotel').child(i).child('RS').get().val()
        RS.append(price)

        image = db.child('hotel').child(i).child('files').get().val()
        files.append(image)

        text = db.child('hotel').child(i).child('abstract').get().val()
        abstract.append(text)

    res = zip(categary, fname, Hname, RS, files,datalist)
    print(res)

    print('Hello', categary)
    print(fname)
    print(Hname)
    print(RS)
    print(files)
    print(abstract)

    return render(HttpRequest, 'edit.html', {'edit': res})


def editdata(HttpRequest):
    db.child('hotel').child


def logindata(HttpRequest):

    email  = HttpRequest.POST.get('email')
    password = HttpRequest.POST.get('password')

    try:
        a = auth.sign_in_with_email_and_password(email,password)
        return HttpResponse('login successfully')

    except:
        return HttpResponse('invalid email or password')


def data(HttpRequest):
    dt = db.child('hotel').shallow().get().val()
    print(dt)

    datalist = []

    for i in dt:
        print(i)
        datalist.append(i)
    datalist.sort(reverse=True)
    print(datalist)

    categary = []
    fname = []
    Hname = []
    RS = []
    files = []
    abstract = []

    for i in datalist:
        cat= db.child('hotel').child(i).child('categary').get().val()
        categary.append(cat)


        name = db.child('hotel').child(i).child('fname').get().val()
        fname.append(name)

        hotelname = db.child('hotel').child(i).child('Hname').get().val()
        Hname.append(hotelname)

        price = db.child('hotel').child(i).child('RS').get().val()
        RS.append(price)

        image = db.child('hotel').child(i).child('files').get().val()
        files.append(image)

        text = db.child('hotel').child(i).child('abstract').get().val()
        abstract.append(text)

    res = zip(categary,fname,Hname,RS,files)
    print(res)


    print('Testing',categary)
    print(fname)
    print(Hname)
    print(RS)
    print(files)
    print(abstract)


    return render(HttpRequest,'data.html',{'data':res})
    #{'cat':categary, 'name':fname, 'hotelname':Hname, 'price':RS, 'image':files, 'text':abstract})



def update(HttpRequest, productid):

    global tid
    tid = productid
    cat = db.child('hotel').child(productid).child('categary').get().val()
    name = db.child('hotel').child(productid).child('fname').get().val()
    hotelname = db.child('hotel').child(productid).child('Hname').get().val()
    price = db.child('hotel').child(productid).child('RS').get().val()
    image = db.child('hotel').child(productid).child('files').get().val()
    text = db.child('hotel').child(productid).child('abstract').get().val()

    print(cat)
    print(name)
    print(hotelname)
    print(price)
    print(image)
    print(text)




    return render(HttpRequest, 'update.html',{'categary': cat,'fname': name,'Hname':hotelname,'RS':price,'files':image,'abstract':text})

def updatedata(HttpRequest):
    cat = HttpRequest.POST.get('categary')
    name = HttpRequest.POST.get('fname')
    hotelname = HttpRequest.POST.get('Hname')
    price = HttpRequest.POST.get('RS')
    image = HttpRequest.POST.get('files')
    text = HttpRequest.POST.get('abstract')

    print(cat)
    print(name)
    print(hotelname)
    print(price)
    print(image)
    print(text)

    db.child('hotel').child(tid).update({'categary': cat, 'fname': name, 'Hname': hotelname, 'RS': price, 'files': image, 'abstract': text})
    return HttpResponse('Data Updated')



def INEEX(HttpRequest):
    return render(HttpRequest, "INEEX.html")

def child(HttpRequest):
    dt = db.child('hotel').shallow().get().val()
    print(dt)

    datalist = []
    counter = 1

    for i in dt:
        print(i)
        datalist.append(i)
    datalist.sort(reverse=True)
    print(datalist)

    categary = []
    fname = []
    Hname = []
    RS = []
    files = []
    abstract = []

    for i in datalist:
        cat = db.child('hotel').child(i).child('categary').get().val()
        categary.append(cat)

        name = db.child('hotel').child(i).child('fname').get().val()
        fname.append(name)

        hotelname = db.child('hotel').child(i).child('Hname').get().val()
        Hname.append(hotelname)

        price = db.child('hotel').child(i).child('RS').get().val()
        RS.append(price)

        image = db.child('hotel').child(i).child('files').get().val()
        files.append(image)

        text = db.child('hotel').child(i).child('abstract').get().val()
        abstract.append(text)

    res = zip(categary, fname,files,Hname, RS, files)
    print(res)

    main_category = set(categary)

    print('test', categary)
    print(fname)
    print(Hname)
    print(RS)
    print(files)
    print(abstract)

    final = {}

    for i in main_category:
        for j in datalist:
            cat = db.child('hotel').child(j).child('categary').get().val()

            if cat == i:

                cat = db.child('hotel').child(j).child('categary').get().val()
                categary.append(cat)

                name = db.child('hotel').child(j).child('fname').get().val()
                fname.append(name)

                hotelname = db.child('hotel').child(j).child('Hname').get().val()
                Hname.append(hotelname)

                price = db.child('hotel').child(j).child('RS').get().val()
                RS.append(price)

                image = db.child('hotel').child(j).child('files').get().val()
                files.append(image)

                text = db.child('hotel').child(j).child('abstract').get().val()
                abstract.append(text)
            final[i]= [name,hotelname,price]
    print('-------------------Final List--------------------')
    print(final)

    return render(HttpRequest, 'child.html', {'data': res,'category':main_category})




#-webkit-animation: mover s infinite  alternate;
 #   animation: mover 0s infinite  alternate;

#'''link
#href = "//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"
#rel = "stylesheet"
#id = "bootstrap-css" >
#< script
#src = "//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" > < / script >
#< script
#src = "//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js" > < / script >'''