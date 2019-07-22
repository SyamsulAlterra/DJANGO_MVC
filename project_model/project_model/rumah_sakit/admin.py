from django.contrib import admin
from django.apps import apps
from .models import *

admin.site.register(Dokter, OrangAdmin)
admin.site.register(Pasien, OrangAdmin)
admin.site.register(Obat, NonOrangAdmin)
admin.site.register(Resep, NonOrangAdmin)
