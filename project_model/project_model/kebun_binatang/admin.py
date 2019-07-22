from django.contrib import admin
from .models import *
from django.apps import apps


admin.site.register(Hewan, HewanAdmin)
admin.site.register(Kandang, HewanAdmin)
admin.site.register(Penjaga, OrangAdmin)
admin.site.register(Pengunjung, OrangAdmin)
