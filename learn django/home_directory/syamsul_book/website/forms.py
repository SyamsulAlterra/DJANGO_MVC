from django.contrib import admin
from django import forms
from .models import *


class person_data(forms.ModelForm):
    class Meta:
        model=Orang
        fields=('username','email','password','name','address')