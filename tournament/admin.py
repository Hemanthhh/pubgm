from django.contrib import admin
from tournament.models import Data
# Register your models here.

from . import models

class DataAdmin(admin.ModelAdmin):
    search_fields = ['name','whatsapp', 'paytm', 'pubg_uid', 'pubg_uname']
    list_display = ['name', 'whatsapp', 'paytm', 'pubg_uid', 'pubg_uname']
    

admin.site.register(Data,DataAdmin)