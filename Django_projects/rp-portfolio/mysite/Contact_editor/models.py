from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class ContactText(models.Model):
    input_text = models.TextField()
    output_text = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    academic_title = models.TextField(blank=True)
    company_name = models.TextField(blank=True)
    position = models.TextField(blank=True)
    street = models.TextField(blank=True)
    house_number = models.TextField(blank=True)
    adress_detail = models.TextField(blank=True)
    zip = models.TextField(blank=True)
    city = models.TextField(blank=True)
    region = models.TextField(blank=True)
    country = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone_number =  models.TextField(blank=True)
    mobile_phone_number = models.TextField(blank=True)
    fax_number = models.TextField(blank=True)
    web_site = models.TextField(blank=True)
    facebook = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    def __str__(self):
        return self.input_text