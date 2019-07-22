from django.contrib import admin
from .models import *

'''
resgister all model using loop
# from django.apps import apps
# app=apps.get_app_config('ata')
# for model_name, model in app.models.items():
#     admin.site.register(model)
'''

admin.site.register(Direksi, OrangAdmin)
admin.site.register(Mentee, OrangAdmin)
admin.site.register(Mentor, OrangAdmin)
admin.site.register(MataPelajaran, MapelAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(LiveCode, ChallengeAdmin)
