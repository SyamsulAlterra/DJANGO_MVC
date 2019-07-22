from django.db import models
from django.contrib import admin
import datetime
# Create your models here.


class OrangAdmin(admin.ModelAdmin):
    list_display=('id','nama', 'nomor_telepon')

class Orang(models.Model):
    nama=models.CharField(max_length=200)
    nomor_telepon=models.CharField('Nomor telepon',max_length=12)

    def __str__(self):
        return self.nama

class Direksi(Orang):
    jabatan=models.CharField(max_length=200)

class Mentee(Orang):
    nomor_absen=models.IntegerField('Nomor absen')
    nilai_rata_rata=models.DecimalField(max_digits=5, decimal_places=2)

class MapelAdmin(admin.ModelAdmin):
    list_display=('id','nama', 'jadwal_mulai', 'jadwal_berakhir')

class ChallengeAdmin(admin.ModelAdmin):
    list_display=('id','nama', 'banyak_soal', 'bobot_nilai')

class Materi(models.Model):
    nama=models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class MataPelajaran(Materi):
    jadwal_mulai=models.DateTimeField('Jadwal mulai')
    jadwal_berakhir=models.DateTimeField('Jadwal berakhir')

class Mentor(Orang):
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class Challenge(Materi):
    banyak_soal=models.IntegerField('Banyak soal')
    bobot_nilai=models.DecimalField('Bobot nilai', max_digits=2, decimal_places=1)
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class LiveCode(Materi):
    tanggal_pelaksanaan=models.DateTimeField('Tanggal Pelaksanaan')
    banyak_soal=models.IntegerField('Banyak soal')
    bobot_nilai=models.DecimalField('Bobot nilai', max_digits=2, decimal_places=1)
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

