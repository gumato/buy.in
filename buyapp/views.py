from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def index(request):
    date = dt.date.today()
    products = Products.objects.all()
    profiles = Profile.objects.all()
    return render(request,'index.html',{"date": date,"products":products})
