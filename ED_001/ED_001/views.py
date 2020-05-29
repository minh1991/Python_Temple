from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse('home')
    return render(req, 'home.html')