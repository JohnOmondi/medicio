from django.shortcuts import render,redirect
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











