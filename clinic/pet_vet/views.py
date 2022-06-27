from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from pet_vet.forms import AppointmentForm
from pet_vet.models import Appointment, Veterinarian


class HomePageView(TemplateView):
    template_name = 'pet_vet/home.html'


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = '/dekujeme/'


class VeterinarianListView(ListView):
    model = Veterinarian


class ContactView(TemplateView):
    template_name = 'pet_vet/contact.html'


class ThanksView(TemplateView):
    template_name = 'pet_vet/thanks.html'
