from django.db import models
from django.contrib import admin
import datetime

# Create your models here.

class OrangAdmin(admin.ModelAdmin):
    list_display=('id','nama','telp', 'alamat')

class Orang(models.Model):
    nama=models.CharField(max_length=200)
    telp=models.CharField(max_length=12)
    alamat=models.TextField('Alamat')

    def __str__(self):
        return self.nama

class Dokter(Orang):
    days=[
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday'),
    ]
    bidang=models.CharField(max_length=200)
    hari_praktik=models.CharField(max_length=3, choices=days)
    jam_praktik=models.TimeField('jadwal')

class Pasien(Orang):
    keluhan=models.TextField('Keluhan')
    tanggal_periksa=models.DateTimeField()

class NonOrangAdmin(admin.ModelAdmin):
    list_display=('id','nama')

class Obat(models.Model):
    nama=models.CharField(max_length=200)
    kandungan=models.TextField('Kandungan')
    khasiat=models.TextField('Khasiat')

    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama=models.CharField(max_length=200)
    total_harga=models.BigIntegerField('Total harga')
    kumpulan_obat=models.TextField()

    def __str__(self):
        return self.nama

