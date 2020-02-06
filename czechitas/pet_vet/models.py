import datetime

from django.core.exceptions import ValidationError
from django.db import models


class Veterinarian(models.Model):
    title_prefix = models.CharField(max_length=32, blank=True, null=True, verbose_name='tituly před')
    first_name = models.CharField(max_length=64, verbose_name='jméno')
    last_name = models.CharField(max_length=64, verbose_name='příjmení')
    title_suffix = models.CharField(max_length=32, blank=True, null=True, verbose_name='tituly za')
    specialization = models.CharField(max_length=128, verbose_name='specializace')

    def __str__(self):
        """E.g. MVDr. John Doe, Ph.D. (Cats, Dogs)"""
        return ' '.join([
            self.title_prefix + ' ' + self.first_name if self.title_prefix else self.first_name,
            self.last_name + ', ' + self.title_suffix if self.title_suffix else self.last_name,
            ' (' + self.specialization + ')'
        ])

    class Meta:
        verbose_name = 'Veterinář'
        verbose_name_plural = 'Veterináři'
        ordering = ['last_name', 'first_name']


class PetType(models.TextChoices):
    SNAKE = 'SNAKE', 'Had'
    CAT = 'CAT', 'Kočka'
    HAMSTER = 'HAMSTER', 'Křeček'
    BIRD = 'PARROT', 'Papoušek'
    DOG = 'DOG', 'Pes'
    WHALE = 'WHALE', 'Velryba'


class Appointment(models.Model):
    date = models.DateField(verbose_name='datum návštěvy')
    name = models.CharField(max_length=128, verbose_name='jméno a příjmení')
    phone = models.CharField(max_length=16, verbose_name='telefon')
    email = models.CharField(max_length=64, blank=True, null=True, verbose_name='e-mail')
    pet_type = models.CharField(max_length=16, choices=PetType.choices, verbose_name='druh mazlíčka')
    preferred_vet = models.ForeignKey(Veterinarian, on_delete=models.PROTECT, verbose_name='preferovaný veterinář')

    class Meta:
        verbose_name = 'Návštěva'
        verbose_name_plural = 'Návštěvy'
        ordering = ['-date', 'pet_type', 'name']

    def __str__(self):
        return f'{self.date} - {self.get_pet_type_display()} - {self.preferred_vet}'

    def clean(self):
        if self.date < datetime.date.today():
            raise ValidationError({'date': 'Datum návštěvy nemůže být v minulosti.'})
