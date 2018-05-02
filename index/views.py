from django.shortcuts import render
from django.http.response import HttpResponse 

# Create your views here.


def login_views(request):
    return render(request,'login.html')
    # return HttpResponse('login index')


def index_views(request):
    return render(request,'index.html')
    # return HttpResponse('main index')


def register_views(request):
    return render(request,'register.html')