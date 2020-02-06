from django.contrib import admin

from pet_vet.models import Appointment, Veterinarian

admin.site.register([Veterinarian, Appointment])
