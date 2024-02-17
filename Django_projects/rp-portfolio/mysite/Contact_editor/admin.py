from django.contrib import admin
# from django-admin.py import collectstatic
# Register your models here.
from .models import ContactText

admin.site.register(ContactText)

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']