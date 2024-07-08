from django.shortcuts import render

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
