from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def homepage(request):
    barangs=Barang.objects.all()
    print(barangs)
    return render(request, 'homepage.html', {'barangs':barangs})

def detail_barang(request, barang_id):
    pilihan=Barang.objects.get(pk=barang_id)
    return render(request, 'detail_barang.html', {'pilihan':pilihan})

def tambah_barang(request):
    if request.method=='POST':
        barang=input_barang(request.POST, request.FILES)
        if barang.is_valid():
            barang.save()
            return redirect('homepage')
    else:
        barang = input_barang()

    return render(request, 'tambah_barang.html',{'barang':barang})