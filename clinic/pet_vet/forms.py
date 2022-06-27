from django.forms import ModelForm
from django.forms.widgets import DateInput, Input

from pet_vet.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'name', 'phone', 'email', 'pet_type', 'preferred_vet']
        widgets = {
            'date': DateInput(attrs={'class': 'input', 'type': 'date'}),
            'name': Input(attrs={'class': 'input', 'placeholder': 'Jan Novák'}),
            'phone': Input(attrs={'class': 'input', 'placeholder': '+420 123 456 789', 'type': 'tel'}),
            'email': Input(attrs={'class': 'input', 'placeholder': 'jan.novak@example.com', 'type': 'email'}),
        }
