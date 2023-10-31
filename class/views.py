from django.http import HttpResponse
from django.shortcuts import render
from .models import Students


# Create your views here.
def home(request):
    return render(request, 'home.html',{'navbar': 'home'})

def contact(request):
    return render(request, 'contacts.html', {'navbar': 'contacts'})

def about(request):
    return render(request, 'about.html', {'navbar': 'about'})

# def settings(request):
#     return render(request, 'hhome.html', {'navbar':'settings'})

def add(request):
    return render(request, 'add.html', {'navbar': 'add'})

def viewdata(request):
    # retrieving data from the DB and storing it in a variable called data
    data = Students.objects.all()
    return render(request, 'viewdata.html', {'navbar': 'viewdata', 'data': data})
