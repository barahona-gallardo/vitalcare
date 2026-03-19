from django.db import models
from django.core.exceptions import ValidationError

from datetime import date

from .choices import SPECIALTY_CHOICES, TIME_CHOICES



class Specialty(models.Model):
    specialty = models.CharField("Especialidad", choices=SPECIALTY_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_specialty_display()


class Availability(models.Model):
    availability = models.CharField("Hora", choices=TIME_CHOICES, unique=True)

    def __str__(self):
        return self.get_availability_display()


class Person(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    date_birth = models.DateField("Fecha de nacimiento")

    @property
    def age(self):
        today = date.today()
        age_years = today.year - self.date_birth.year
        age_adjustment = (today.month, today.day) < (
            self.date_birth.month,
            self.date_birth.day,
        )
        age = age_years - age_adjustment
        return age
    
    def clean(self):
        if self.date_birth > date.today():
            raise ValidationError("Fecha de nacimiento inválida.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(Person):
    pass


class Provider(Person):
    specialty = models.ForeignKey(
        Specialty, verbose_name="Especialidad", on_delete=models.PROTECT
    )


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, verbose_name="Paciente", related_name="patient", on_delete=models.PROTECT
    )
    provider = models.ForeignKey(
        Provider, verbose_name="Especialista", related_name="provider", on_delete=models.PROTECT
    )
    date = models.DateField("Fecha")
    time = models.ForeignKey(
        Availability, verbose_name="Hora", related_name="time", on_delete=models.PROTECT
    )
    reason = models.ForeignKey(
        Specialty, verbose_name="Motivo", related_name="reason", on_delete=models.PROTECT
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["patient", "provider", "time"], name="unique_appointment"
            )
        ]

    def clean(self):
        if self.date < date.today():
            raise ValidationError("Fecha de agendamiento inválida.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.time.availability} - {self.patient.first_name} {self.patient.last_name} - {self.provider.first_name} {self.provider.last_name} - {self.reason}"
