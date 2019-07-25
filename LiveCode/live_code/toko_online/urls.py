from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('barang/<int:barang_id>', views.detail_barang, name='detail barang'),
    path('barang/tambah/', views.tambah_barang, name='tambah barang'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)