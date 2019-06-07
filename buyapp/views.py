from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Category,Product
from django.contrib.auth.decorators import login_required
from tinymce.models import HTMLField

# Create your views here.
def index(request):
    date = dt.date.today()
    # profiles = Profile.objects.all()
    products = Product.objects.all()
    cat=Category.objects.all()
    return render(request,'index.html',{'cat':cat,'products':products})


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                to_email = form.cleaned_data.get('email')
                return HttpResponse('Confirm your email address to complete registration')
           
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'Form':form})


def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        search_category = Category.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'categories':search_category})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
@login_required(login_url='/accounts/login/')
def product(request):
    category = None
    category = Category.objects.all()
def categories(request,id):
    title='Category'
    products = Product.objects.filter(id=id)
    
    return render(request,'category.html',{'title':title,'products':products})

