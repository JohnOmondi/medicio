from django.shortcuts import render,redirect
from runserver.models import Contacts
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
        all = Contacts(name=request.POST['name'],email=request.POST['email'],phone=request.POST['phone'],message=request.POST['message'])
        all.save()
        return redirect('/contact')
    else:
        return render(request,'Contact.html')
