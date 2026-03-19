from django import forms

from .models import Patient, Provider, Appointment



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient", "provider", "date", "time", "reason"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "date_birth"]
        widgets = {
            "date_birth": forms.DateInput(attrs={"type": "date"})
        }


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ["first_name", "last_name", "date_birth", "specialty"]
        widgets = {
            "date_birth": forms.DateInput(attrs={"type": "date"})
        }
