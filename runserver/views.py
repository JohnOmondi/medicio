import json

import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests.auth import HTTPBasicAuth

from runserver.credentials import LipanaMpesaPpassword, MpesaAccessToken
from runserver.models import Contacts, appointment, Members, ImageModel
from runserver.forms import appointmentForm, ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        if Members.objects.filter(username=request.POST['username'],
                                  password=request.POST['password']


            ).exists():
            members = Members.objects.get(username=request.POST['username'],
                                         password=request.POST['password'])
            return  render(request, 'index.html',{'members':members})
        else:
             return  render(request, 'login.html')
    else:
        return render(request, 'login.html')










def inner(request):
    return render(request,'inner-page.html')


def About(request):
    return render(request,'About.html')

def doctors(request):
    return render(request,'doctors.html')

def department(request):
    return render(request,'department.html')

def contact(request):
    if request.method == 'POST':
        all = Contacts(name=request.POST['name'],
                       email=request.POST['email'],
                       phone=request.POST['phone'],
                       message=request.POST['message'])
        all.save()
        return redirect('/contact')
    else:
        return render(request,'Contact.html')



def Appointment(request):
     if request.method == 'POST':
        appointments = appointment(name=request.POST['name'],
                          email=request.POST['email'],
                          phone=request.POST['phone'],
                          date=request.POST['date'],
                          department=request.POST['department'],
                          doctor=request.POST['doctor'],
                          message=request.POST['message'])


        appointments.save()
        return redirect('/show')
     else:
          return render(request, 'appointment.html')


def show(request):
    information = appointment.objects.all()
    return render(request,'show.html',{'data':information})

def delete(request,id):
    myappointment = appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')


def edit(request,id):
    Appointment = appointment.objects.get(id=id)
    return render(request,'edit.html',{'x':appointment})

def update(request,id):
    if request.method == 'POST':
        Appointment = appointment.objects.get(id=id)
        form = appointmentForm(request.POST, instance=Appointment)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
         return render(request,'edit.html')

    else:
         return render(request,'edit.html')



def register(request):
    if request.method == 'POST':
        members=Members(name=request.POST['name'],
                        username=request.POST['username'],
                        password=request.POST['password'],)

        members.save()
        return redirect('/login')
    else:
        return  render(request,'register.html')


def login(request):
   return render(request,'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")





















