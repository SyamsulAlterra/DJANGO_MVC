from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama=models.CharField(max_length=200)
    spesies=models.CharField(max_length=200)
    berat=models.DecimalField(decimal_places=2, max_digits=6)
    umur=models.IntegerField()

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama=models.CharField(max_length=200)
    isi_kandang=Hewan()
    luas_kandang=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Orang(models.Model):
    nama=models.CharField(max_length=200)
    nomor_telepon=models.BigIntegerField('Nomor telepon')

    def __str__(self):
        return self.nama
    
class Penjaga(Orang):
    days=[
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday'),
    ]
    hari_jaga=models.CharField(choices=days, max_length=3)
    mulai_jaga=models.TimeField()
    selesai_jaga=models.TimeField()

class Pengunjung(Orang):
    hari_berkunjung=models.DateTimeField('Hari berkunjung')

