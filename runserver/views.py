from django.shortcuts import render,redirect
from runserver.models import Contacts,appointment
from runserver.forms import appointmentForm
# Create your views here.
def index(request):
   return render(request,'index.html')

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
   return render(request,'register.html')


def login(request):
   return render(request,'login.html')








