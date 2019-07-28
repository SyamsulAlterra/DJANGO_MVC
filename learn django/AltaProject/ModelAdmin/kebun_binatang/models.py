from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama=models.CharField(max_length=200)
    spesies=models.CharField(max_length=200)
    berat=models.IntegerField('Berat')
    umur=models.IntegerField('Umur')

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama=models.CharField(max_length=200)
    isi_kandang=Hewan()
    luas_kandang=models.IntegerField('Luas Kandang')

    def __str__(self):
        return self.nama

class Orang(models.Model):
    nama=models.CharField(max_length=200)
    nomor_telepon=models.IntegerField('Nomor telepon')

    def __str__(self):
        return self.nama
    
class Penjaga(Orang):
    jadwal_jaga=models.DateTimeField('Jadwal jaga')

class Pengunjung(Orang):
    hari_berkunjung=models.DateTimeField('Hari berkunjung')

