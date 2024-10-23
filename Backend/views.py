from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Backend.models import country_db,place_db,offer_db,package_db,placeDetails_db,hotel_db,flight_db
from Frontend.models import contact_db
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def indexpage(req):
    return render(req,"index.html")

def addcountry(req):
    return render(req,"addcountry.html")

def save_addcountry(req):
    if req.method=="POST":
        cn = req.POST.get('country')
        ci = req.FILES['img']
        np = req.POST.get('no')
        obj = country_db(Country=cn,Image=ci,No_tour_place=np)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(addcountry)

def dis_addcountry(req):
    country = country_db.objects.all()
    return render(req,"display_addcountry.html",{'country':country})

def edit_country(req,dataid):
    country = country_db.objects.get(id=dataid)
    return render(req,"edit_addcountry.html",{'country':country})

def update_country(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('country')
        try:
            ci = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(ci.name,ci)
        except MultiValueDictKeyError:
            file = country_db.objects.get(id=dataid).Image
        np = req.POST.get('no')
        country_db.objects.filter(id=dataid).update(Country=cn,Image=file,No_tour_place=np)
        messages.success(req, "Data Updated successfully")
        return redirect(dis_addcountry)
    messages.error(req, "Update failed")


def delete_country(req,dataid):
    country = country_db.objects.filter(id=dataid)
    country.delete()
    messages.success(req, "Data removed")
    return redirect(dis_addcountry)

def adminlogin(req):
    return render(req,"adminlogin.html")

def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pw = request.POST.get('psw')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pw)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pw
                messages.success(request, "login successful")
                return redirect(indexpage)
            else:
                messages.error(request, "login failed")
                return redirect(adminlogin)
        else:
            messages.success(request, "Login failed")
            return redirect(adminlogin)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logged out")
    return redirect(adminlogin)

def addplace(req):
    country = country_db.objects.all()
    return render(req,"addplaces.html",{'country':country})

def save_place(req):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        pi = req.FILES['img']
        des = req.POST.get('details')
        na = req.POST.get('name')
        obj = place_db(Country=cn,Place=pn,Image=pi,Description=des,Name=na)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(addplace)
    messages.error(req, "Failed to add")


def dis_place(req):
    place = place_db.objects.all()
    return render(req,"display_addplace.html",{'place':place})

def edit_place(req,dataid):
    country = country_db.objects.all()
    place = place_db.objects.get(id=dataid)
    return render(req,"edit_addplace.html",{'country':country,'place':place})

def update_place(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        try:
            pi = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(pi.name,pi)
        except MultiValueDictKeyError:
            file = place_db.objects.get(id=dataid).Image
        des = req.POST.get('details')
        na = req.POST.get('name')
        place_db.objects.filter(id=dataid).update(Country=cn,Place=pn,Image=file,Description=des,Name=na)
        messages.success(req, "Data Updated")
        return redirect(dis_place)
    messages.success(req, "Failed to update")


def delete_place(req,dataid):
    place = place_db.objects.filter(id=dataid)
    place.delete()
    messages.success(req, "Data removed")
    return redirect(dis_place)


def addspecial_offer(req):
    country = country_db.objects.all()
    return render(req,"addspecialoffer.html",{'country':country})


def save_offer(req):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        des = req.POST.get('details')
        rate = req.POST.get('rate')
        h = req.POST.get('hotel')
        rs = req.POST.get('price')
        dis = req.POST.get('discount')
        p1 = req.FILES['img1']
        p2 = req.FILES['img2']
        p3 = req.FILES['img3']
        p4 = req.FILES['img4']
        obj = offer_db(Country=cn,Place=pn,Details=des,Rating=rate,Hotel=h,price=rs,Discount=dis,Image1=p1,Image2=p2,Image3=p3,Image4=p4)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(addspecial_offer)


def dis_offers(req):
    offers = offer_db.objects.all()
    return render(req,"display_specialoffer.html",{'offers':offers})

def edit_offers(req,dataid):
    offers = offer_db.objects.get(id=dataid)
    return render(req,"edit_specialoffers.html",{'offers':offers})

def update_offer(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        des = req.POST.get('details')
        rate = req.POST.get('rate')
        h = req.POST.get('hotel')
        rs = req.POST.get('price')
        dis = req.POST.get('discount')
        try:
            p1 = req.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(p1.name,p1)
        except MultiValueDictKeyError:
            file1 = offer_db.objects.get(id=dataid).Image1
        try:
            p2 = req.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(p2.name,p2)
        except MultiValueDictKeyError:
            file2 = offer_db.objects.get(id=dataid).Image2
        try:
            p3 = req.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(p3.name,p3)
        except MultiValueDictKeyError:
            file3 = offer_db.objects.get(id=dataid).Image3
        try:
            p4 = req.FILES['img4']
            fs = FileSystemStorage()
            file4 = fs.save(p4.name,p4)
        except MultiValueDictKeyError:
            file4 = offer_db.objects.get(id=dataid).Image4
        offer_db.objects.filter(id=dataid).update(Country=cn,Place=pn,Details=des,Rating=rate,Hotel=h,price=rs,Discount=dis,Image1=file1,Image2=file2,Image3=file3,Image4=file4)
        messages.success(req, "Data updated")
        return redirect(dis_offers)

def delete_offers(req,dataid):
    offers = offer_db.objects.filter(id=dataid)
    offers.delete()
    messages.success(req, "Data removed")
    return redirect(dis_offers)


def addpackages(req):
    country = country_db.objects.all()
    return render(req,"add_packages.html",{'country':country})

def save_package(req):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        des = req.POST.get('details')
        rate = req.POST.get('rate')
        h = req.POST.get('hotel')
        rs = req.POST.get('price')
        dis = req.POST.get('discount')
        p1 = req.FILES['img1']
        p2 = req.FILES['img2']
        p3 = req.FILES['img3']
        p4 = req.FILES['img4']
        obj = package_db(Country=cn,Place=pn,Details=des,Rating=rate,Hotel=h,price=rs,Discount=dis,Image1=p1,Image2=p2,Image3=p3,Image4=p4)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(addpackages)

def dis_package(req):
    package = package_db.objects.all()
    return render(req,"display_packages.html",{'package':package})

def edit_package(req,dataid):
    country = country_db.objects.all()
    package = package_db.objects.get(id=dataid)
    return render(req,"edit_package.html",{'package':package,'country':country})


def update_package(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        des = req.POST.get('details')
        rate = req.POST.get('rate')
        h = req.POST.get('hotel')
        rs = req.POST.get('price')
        dis = req.POST.get('discount')
        try:
            p1 = req.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(p1.name,p1)
        except MultiValueDictKeyError:
            file1 = package_db.objects.get(id=dataid).Image1
        try:
            p2 = req.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(p2.name,p2)
        except MultiValueDictKeyError:
            file2 = package_db.objects.get(id=dataid).Image2
        try:
            p3 = req.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(p3.name,p3)
        except MultiValueDictKeyError:
            file3 = package_db.objects.get(id=dataid).Image3
        try:
            p4 = req.FILES['img4']
            fs = FileSystemStorage()
            file4 = fs.save(p4.name,p4)
        except MultiValueDictKeyError:
            file4 = package_db.objects.get(id=dataid).Image4
        package_db.objects.filter(id=dataid).update(Country=cn,Place=pn,Details=des,Rating=rate,Hotel=h,price=rs,Discount=dis,Image1=file1,Image2=file2,Image3=file3,Image4=file4)
        messages.success(req, "Data updated")
        return redirect(dis_package)

def delete_package(req,dataid):
    package = package_db.objects.filter(id=dataid)
    package.delete()
    messages.success(req, "Data removed")
    return redirect(dis_package)


def add_place_details(req):
    place = place_db.objects.all()
    return render(req,"add_place_details.html",{'place':place})

def save_place_details(req):
    if req.method=="POST":
        pl = req.POST.get('place')
        co = req.POST.get('country')
        de = req.POST.get('details')
        img = req.FILES['img']
        obj = placeDetails_db(Place=pl,Country=co,Details=de,Image=img)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(add_place_details)

def dis_pdetails(req):
    details = placeDetails_db.objects.all()
    return render(req,"display_place_details.html",{'details':details})

def edit_pdetails(req,dataid):
    details = placeDetails_db.objects.get(id=dataid)
    return render(req,"edit_place_details.html",{'details':details})

def update_pdetails(req,dataid):
    if req.method=="POST":
        pl = req.POST.get('place')
        co = req.POST.get('country')
        de = req.POST.get('details')
        try :
            img = req.FILES['img']
            fs =FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = placeDetails_db.objects.get(id=dataid).Image
        placeDetails_db.objects.filter(id=dataid).update(Place=pl,Country=co,Details=de,Image=file)
        messages.success(req, "Data updated")
        return redirect(dis_pdetails)

def delete_pdetails(req,dataid):
    details = placeDetails_db.objects.filter(id=dataid)
    details.delete()
    messages.success(req, "Data removed")
    return redirect(dis_pdetails)


def add_hotel(req):
    country = country_db.objects.all()
    place = place_db.objects.all()
    return render(req,"add_hotels.html",{'country':country,'place':place})

def save_Hotel(req):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        des = req.POST.get('details')
        rate = req.POST.get('rate')
        h = req.POST.get('hotel')
        rs = req.POST.get('price')
        dis = req.POST.get('discount')
        p1 = req.FILES['img1']
        p2 = req.FILES['img2']
        p3 = req.FILES['img3']
        p4 = req.FILES['img4']
        loc = req.POST.get('location')
        obj = hotel_db(Country=cn,Place=pn,Details=des,Rating=rate,Hotel=h,price=rs,Discount=dis,Image1=p1,Image2=p2,Image3=p3,Image4=p4,Location=loc)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(add_hotel)

def dis_hotel(req):
    hotel = hotel_db.objects.all()
    return render(req,"display_hotel.html",{'hotel':hotel})

def edit_hotel(req,dataid):
    hotel = hotel_db.objects.get(id=dataid)
    country = country_db.objects.all()
    place = place_db.objects.all()
    return render(req,"edit_hotel.html",{'hotel':hotel,'country':country,'place':place})


def update_hotel(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('country')
        pn = req.POST.get('Place')
        des = req.POST.get('details')
        rate = req.POST.get('rate')
        h = req.POST.get('hotel')
        rs = req.POST.get('price')
        dis = req.POST.get('discount')
        try:
            p1 = req.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(p1.name,p1)
        except MultiValueDictKeyError:
            file1 = hotel_db.objects.get(id=dataid).Image1
        try:
            p2 = req.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(p2.name,p2)
        except MultiValueDictKeyError:
            file2 = hotel_db.objects.get(id=dataid).Image2
        try:
            p3 = req.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(p3.name,p3)
        except MultiValueDictKeyError:
            file3 = hotel_db.objects.get(id=dataid).Image3
        try:
            p4 = req.FILES['img4']
            fs = FileSystemStorage()
            file4 = fs.save(p4.name,p4)
        except MultiValueDictKeyError:
            file4 = hotel_db.objects.get(id=dataid).Image4
        loc = req.POST.get('location')
        hotel_db.objects.filter(id=dataid).update(Country=cn,Place=pn,Details=des,Rating=rate,Hotel=h,price=rs,Discount=dis,Image1=file1,Image2=file2,Image3=file3,Image4=file4,Location=loc)
        messages.success(req, "Data updated")
        return redirect(dis_hotel)


def delete_hotel(req,dataid):
    hotel = hotel_db.objects.filter(id=dataid)
    hotel.delete()
    messages.success(req, "Data removed")
    return redirect(dis_hotel)


def addflight(req):
    return render(req,"add_flight.html")

def save_addflight(req):
    if req.method=="POST":
        fr = req.POST.get('from')
        to = req.POST.get('Destination')
        fp = req.POST.get('sCity')
        fc = req.POST.get('sCountry')
        tp = req.POST.get('eCity')
        tc = req.POST.get('eCountry')
        fl = req.POST.get('Flight')
        fn = req.POST.get('Flightno')
        de = req.POST.get('Departure')
        la = req.POST.get('Arrival')
        ch = req.POST.get('Charge')
        obj = flight_db(From=fr,To=to,From_City=fp,From_country=fc,To_city=tp,To_Country=tc,
                        Flight_name=fl,Flight_No=fn,Depature_time=de,Landing_time=la,Charge=ch)
        obj.save()
        messages.success(req, "Data added successfully")
        return redirect(addflight)

def flight_detail(request):
    flight = flight_db.objects.all()
    return render(request,"display_flight.html",{'flight':flight})

def contact_details(request):
    contact = contact_db.objects.all()
    return render(request,"display_message.html",{'contact':contact})

def delete_contact_details(request,dataid):
    contact = contact_db.objects.filter(id=dataid)
    contact.delete()
    return redirect(contact_details)