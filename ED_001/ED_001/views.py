from django.http import HttpResponse
from django.shortcuts import render
from app_news.models import News


def home(req):
    # Select all DB
    home_obj_ls = News.objects.all()
    return render(req, 'home.html', {
        'home_obj_ls': home_obj_ls,
        'nav': 'home'
    })


def About(req):
    return render(req, 'about.html', {
        'nav': 'about'
    })
