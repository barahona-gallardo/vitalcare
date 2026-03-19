from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .choices import SPECIALTY_CHOICES, generate_time_choices
from .models import Appointment, Availability, Patient, Person, Provider, Specialty

class PersonModelTest(TestCase):
    def test_date_birth(self):    
        with self.assertRaises(ValidationError):
            Person.objects.create(
                first_name = "John",
                last_name = "Doe",
                date_birth = date(2080, 8, 8)
            )

    # def test_instance(self):
    #     self.person = Person.objects.create(
    #         first_name = "John",
    #         last_name = "Doe",
    #         date_birth = date(1980, 8, 8)
    #     )
    #     return self.person

#     def test_str(self):
#         person = self.test_instance()
#         self.assertEqual(str(person), f"{person.first_name} {person.last_name}")


class SpecialtyModelTest(TestCase):
    def test_instance(self):
        self.specialty = Specialty.objects.create(
            specialty = SPECIALTY_CHOICES[0]
        )
        return self.specialty
    
    def test_unique(self):
        self.test_instance()
        with self.assertRaises(IntegrityError):
            Specialty.objects.create(
            specialty = SPECIALTY_CHOICES[0]
        )


class AppointmentModelTest(TestCase):
    def test_date_appoinment(self):        
        specialty = Specialty.objects.create(specialty = SPECIALTY_CHOICES[0])
        patient = Patient.objects.create(first_name = "John", last_name = "Doe", date_birth=date(2000, 1, 1))
        provider = Provider.objects.create(first_name = "John", last_name = "Doe", date_birth=date(2000, 1, 1), specialty=specialty)
        time = Availability.objects.create(availability = generate_time_choices()[0]) 
        
        with self.assertRaises(ValidationError):
            Appointment.objects.create(
                    patient = patient,
                    provider = provider,
                    date = date.today() - timedelta(days=1),
                    time = time,
                    reason = specialty
                )
