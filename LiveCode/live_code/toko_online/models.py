from django.db import models


class Barang(models.Model):
    nama=models.CharField(max_length=200)
    foto=models.ImageField(upload_to='foto_barang')
    harga=models.IntegerField('Rupiah')
    link_detail=models.CharField(max_length=200, default='lihat detail')
    deskripsi=models.TextField('deskripsi', blank=True)

    def __str__(self):
        return self.nama

    