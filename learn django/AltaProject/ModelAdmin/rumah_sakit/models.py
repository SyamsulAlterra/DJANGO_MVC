from django.db import models
import datetime

# Create your models here.
class Orang(models.Model):
    nama=models.CharField(max_length=200)
    telp=models.IntegerField('Nomor Telepon')
    alamat=models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class Dokter(Orang):
    bidang=models.CharField(max_length=200)
    jadwal=models.DateTimeField('Jadwal Praktik')

class Pasien(Orang):
    keluhan=models.CharField(max_length=200)

class Resep(models.Model):
    nama=models.CharField(max_length=200)
    total_harga=models.IntegerField('Total harga')
    kumpulan_obat='tes'

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama=models.CharField(max_length=200)
    kandungan=models.TextField('Kandungan')
    khasiat=models.TextField('Khasiat')

    def __str__(self):
        return self.nama
