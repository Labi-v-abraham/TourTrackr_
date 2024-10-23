import json

from django.shortcuts import render,redirect
from Backend.models import country_db,place_db,offer_db,placeDetails_db,hotel_db,flight_db,package_db
from Frontend.models import register_db,hotel_booking_db,blog_db,subscription_db,sub_payment,review_db,flight_booking_db,contact_db
from django.contrib import messages
from datetime import datetime
import razorpay
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from TourTrackr import settings
from decimal import Decimal


# Create your views here.

def homepage(request):
    country = country_db.objects.all()[:6]
    hotelc = country_db.objects.all()
    flight = flight_db.objects.values('From').distinct()
    flighto = flight_db.objects.values('To').distinct()
    review = review_db.objects.all()
    sub = subscription_db.objects.filter(user=request.session['Username'])
    offers = offer_db.objects.all()
    package = package_db.objects.all()

    return render(request,"home.html",{'country':country,'hotelc':hotelc,'flight':flight,'flighto':flighto,'review':review,'sub':sub,'offers':offers,'package':package})

def destination(req):
    country = country_db.objects.all()
    return render(req,"destination.html",{'country':country})

def place(request,cname):
    place = place_db.objects.filter(Country=cname)
    return render(request,"place.html",{'place':place})

def login_page(request):
    return render(request,"login.html")

def register_page(request):
    return render(request,"register.html")

def save_register(request):
    if request.method=="POST":
        un = request.POST.get('username')
        em = request.POST.get('email')
        mo = request.POST.get('mob')
        pa = request.POST.get('password')
        obj = register_db(Username=un,Email=em,Mobile=mo,Password=pa)
        obj.save()
        return redirect(login_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        psw = request.POST.get('password')
        if register_db.objects.filter(Username=un,Password=psw).exists():
            request.session['Username'] = un
            request.session['Password'] = psw
            return redirect(homepage)
        else:
            messages.error(request, "Login Failed")
            return redirect(login_page)
    return redirect(login_page)


def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logged out")
    return redirect(login_page)

def placedetails(req,pname):
    details = placeDetails_db.objects.filter(Place=pname)
    hotel = hotel_db.objects.filter(Place=pname)
    return render(req,"placeDetails.html",{'details':details,'hotel':hotel})

def hotel(req):
    if req.method=="POST":
        searched = req.POST['hotel']
        hotel = hotel_db.objects.filter(Country__icontains=searched)
        return render(req,"hotel.html",{'hotel':hotel,'searched':searched})


def flight(req):
    if req.method=="POST":
        destination = req.POST['from']
        to = req.POST['to']
        flight = flight_db.objects.filter(From__contains=destination,To__contains=to)
        return render(req,"flight.html",{'destination':destination,'to':to,'flight':flight})

def book_flight(req,dataid):
    flight = flight_db.objects.get(id=dataid)
    return render(req,"book_flight.html",{'flight':flight})

def save_book_flight(request):
    if request.method == "POST":
        na = request.POST.get('user')
        fn = request.POST.get('fname')
        sn = request.POST.get('lname')
        em = request.POST.get('email')
        cl = request.POST.get('Class')
        ad = request.POST.get('guests')
        da = request.POST.get('date')
        fl = request.POST.get('flight')
        fln = request.POST.get('fno')
        pr = request.POST.get('tprice')
        ti = request.POST.get('time')
        obj = flight_booking_db(name=na,First_name=fn,Second_name=sn,Email=em,Type=cl,No_person=ad,Date=da,Flight=fl,Flight_no=fln,Price=pr,Time=ti)
        obj.save()
        return redirect(flight_payment)

def flight_payment(request):
    last_object = flight_booking_db.objects.order_by('-id').first()
    payy = last_object.Price
    if request.method == "POST":
        amount = int(last_object.Price)
        order_currency = 'INR'
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
    return render(request,"flight_payment.html",{'payy':payy,'last_object':last_object})


def select_hotel(req,dataid):
    hotel = hotel_db.objects.get(id=dataid)
    return render(req,"select_hotel.html",{'hotel':hotel})


def hotel_booking(req,dataid):
    hotel = hotel_db.objects.get(id=dataid)
    return render(req,"Hotel_booking.html",{'hotel':hotel})

def save_hotelBooking(request):
    if request.method=="POST":
        us = request.POST.get('user')
        hn = request.POST.get('hotel')
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        em = request.POST.get('email')
        ro = request.POST.get('room')
        no = request.POST.get('guests')
        ad = request.POST.get('date')
        at = request.POST.get('time')
        ti = request.POST.get('ap')
        ch = request.POST.get('out')
        pi = request.POST.get('radio')
        fi = request.POST.get('flight')
        re = request.POST.get('request')
        pr = request.POST.get('price')
        bi = request.POST.get('tprice')
        obj = hotel_booking_db(User=us,Hotel_name=hn,First_name=fn,Second_name=ln,Email=em,No_of_guest=no,Arrive_date=ad,Arrive_time=at,
                               Arrive_apm=ti,Checkout=ch,Pickup=pi,Flight=fi,Request=re,Price=pr,Bill=bi,Room=ro)

        obj.save()
        return redirect(h_payment)

def h_payment(request):
    last_object = hotel_booking_db.objects.order_by('-id').first()
    payy = last_object.Bill
    payy_str = str(payy)
    for ptotl in payy_str:
        print(ptotl)

    if request.method == "POST":
        amount = int(last_object.bill)
        order_currency = 'INR'
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1','redirect': 'http://127.0.0.1:9000/Frontend/rating/',})
    return render(request,"hotel_payment.html",{'payy_str':payy_str,'last_object':last_object})

def rating(request):
    return render(request,"rating.html")

def rating_save(request):
    if request.method=="POST":
        na = request.POST.get('name')
        ra = request.POST.get('rating')
        de = request.POST.get('description')
        obj = review_db(name=na,rating=ra,description=de)
        obj.save()
        return redirect(homepage)

def success(req):
    return render(req,"success.html")


def blogs(req):
    blog = blog_db.objects.all()
    return render(req,"blogs.html",{'blog':blog})

def createBlog(req):
    today = datetime.now().strftime('%Y-%m-%d')
    return render(req,"createBlog.html",{'today':today})

def save_createBlog(req):
    if req.method=="POST":
        un = req.POST.get('user')
        da = req.POST.get('date')
        img1 = req.FILES['photo']
        img2 = req.FILES['photo1']
        ti = req.POST.get('title')
        su = req.POST.get('summary')
        de = req.POST.get('write')
        obj = blog_db(user=un,date=da,image1=img1,image2=img2,title=ti,summary=su,detail=de)
        obj.save()
        messages.success(req, "Blog created")
        return redirect(blogs)

def blog_details(req,dataid):
    blog = blog_db.objects.get(id=dataid)
    return render(req,"blog_details.html",{'blog':blog})


def subscription(req):

    if req.method=="POST":
        un = req.POST.get('user')
        em = req.POST.get('email')
        obj = subscription_db(user=un,email=em)
        obj.save()
        return render(req,"subscription.html")

def subscription_form(request):
    if request.method == "POST":
        na = request.POST.get('name')
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        data = {"amount": 399, "currency": "INR", "receipt": "1"}
        payment = client.order.create(data=data)
        obj = sub_payment(name=na,amount=399,payment_id=payment['id'])
        try:

            obj.save()
            messages.success(request, "Subscribed successfully")
            return redirect(homepage)
        except Exception as e:
            print(f"Error saving subscription data: {e}")
            messages.error(request,"failed to save")
    return redirect(homepage)

@csrf_exempt
def sub_success(req):
    if req.method =="POST":
        return redirect(homepage)
    return redirect(homepage)

def profile(request,user):
    user_na = register_db.objects.filter(Username=user)
    sub = subscription_db.objects.filter(user=request.session['Username'])

    return render(request,"profile.html",{'user_na':user_na,'sub':sub})



def edit_profile(req):
    if req.method=="POST":
        user = req.POST.get('user')
        data = register_db.objects.filter(Username__contains=user)
        return render(req,"edit_profile.html",{'data':data})


def update_profile(request):
    if request.method=="POST":
        na = request.POST.get('username')
        fu = request.POST.get('name')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        mo = request.POST.get('mobile')
        pl = request.POST.get('place')
        co = request.POST.get('country')
        register_db.objects.filter(Username=request.session['Username']).update(Username=na,Email=em,Mobile=mo,Password=ps,Place=pl,Country=co,Name=fu)
        messages.success(request, "Data updated")
        return redirect(login_page)


def send_email(request):
    if request.method == 'POST':
        # Extract user email from the POST data (assuming the button click provides the email)
        user_email = request.POST.get('email')

        latest_data = hotel_booking_db.objects.latest('id')

        # Send email
        subject = 'Hotel Booked'
        message = f"Hotel Name: {latest_data.Hotel_name}\n\nName: {latest_data.First_name} {latest_data.Second_name}\n\nRoom: {latest_data.Room} \n\nCheckin & checkout date: {latest_data.Arrive_date} and {latest_data.Checkout}\n\n" \
                  f"Thank you for Booking "
        from_email = settings.EMAIL_HOST
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list)

        return redirect(rating)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)


def flight_email(request):
    if request.method == 'POST':
        # Extract user email from the POST data (assuming the button click provides the email)
        user_email = request.POST.get('email')

        latest_data = flight_booking_db.objects.latest('id')

        # Send email
        subject = 'Flight Ticket'
        message = f"Name: {latest_data.First_name} {latest_data.Second_name}\n\nFlight: {latest_data.Flight}\n\nFlight No: {latest_data.Flight_no} \n\nClass: {latest_data.Type}\n\nNo.of passengers: {latest_data.No_person}\n\nDate & time: {latest_data.Date} & {latest_data.Time}\n\n" \
                  f"Thank you for Booking "
        from_email = settings.EMAIL_HOST
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list)

        return redirect(rating)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)


def contact(request):
    return render(request,"contact.html")

def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ms = request.POST.get('message')
        obj = contact_db(Name=na,Email=em,Message=ms)
        obj.save()
        messages.success(request,"message delivered")
        return redirect(contact)


def Offers_booking(request):
    return render(request,"offer_booking.html")

def offer_details(request,dataid):
    offer = offer_db.objects.get(id=dataid)
    return render(request,"offer_details.html",{'offer':offer})

def package_booking(request):
    return render(request,"package_booking.html")


