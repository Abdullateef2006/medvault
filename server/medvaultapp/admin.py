from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CustomUser)
admin.site.register(EmergencyProfile)
admin.site.register(QRCode)     