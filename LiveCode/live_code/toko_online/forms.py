from django import forms
from .models import *

class input_barang(forms.ModelForm):
    class Meta:
        model=Barang
        fields=('nama', 'foto', 'harga', 'deskripsi')