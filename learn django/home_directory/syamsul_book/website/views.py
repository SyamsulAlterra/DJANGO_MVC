from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

def welcome_page(request):
    return render(request, 'welcome_page.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up(request):
    if request.method=='POST':
        data=person_data(request.POST)
        if data.is_valid():
            data.save()
            return redirect('success sign up')
    else:
        data=person_data()

    # return HttpResponseRedirect('/')
    return render(request, 'sign_up.html', {'data':data})

def success_sign_up(request):
    return render(request, 'success_sign_up.html')

def homepage(request):
    if request.method == 'POST':
        
        pengguna = Orang.objects.all()
        