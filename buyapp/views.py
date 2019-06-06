from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def index(request):
    date = dt.date.today()
    # products = Products.objects.all()
    # profiles = Profile.objects.all()
    return render(request,'index.html')
