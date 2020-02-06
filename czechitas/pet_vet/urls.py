"""pet_vet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from pet_vet import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sjednat-schuzku/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('nasi-veterinari/', views.VeterinarianListView.as_view(), name='veterinarian-list'),
    path('kontakty/', views.ContactView.as_view(), name='contact'),
    path('dekujeme/', views.ThanksView.as_view(), name='thanks'),
]
