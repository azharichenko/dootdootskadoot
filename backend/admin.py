from django.contrib import admin
from backend.models import *

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Treatment)
admin.site.register(Diagnosis)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Diet)
admin.site.register(Environment)
admin.site.register(Actions)