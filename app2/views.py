from django.shortcuts import render


# Create your views here.

def hhome(request):
    return render(request, 'hhome.html',{'navbar': 'settings'})
