from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title','date_created','phone_number']
    list_filter = ['date_created']
    search_fields = ["title"]
