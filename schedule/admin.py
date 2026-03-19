from django.contrib import admin

from .models import Specialty, Availability, Provider, Patient, Appointment

admin.site.register([Specialty, Availability, Provider, Patient, Appointment])