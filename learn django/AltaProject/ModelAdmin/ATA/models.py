from django.db import models
import datetime

# Create your models here.
class Orang(models.Model):
    nama=models.CharField(max_length=200)
    nomor_telepon=models.IntegerField('Nomor telepon')

    def __str__(self):
        return self.nama

class Direksi(Orang):
    jabatan=models.CharField(max_length=200)

class Mentee(Orang):
    nomor_absen=models.IntegerField('Nomor absen')
    nilai_rata_rata=models.IntegerField('Nilai rata-rata')

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
    bobot_nilai=models.IntegerField('Bobot nilai')
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class LiveCode(Materi):
    tanggal_pelaksanaan=models.DateTimeField('Tanggal Pelaksanaan')

