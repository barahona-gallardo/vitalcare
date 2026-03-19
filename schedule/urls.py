from django.urls import path

from . import views



app_name = "schedule"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("provider/create", views.ProviderCreateView.as_view(), name="provider_create"),
    path("provider/update/<int:pk>", views.ProviderUpdateView.as_view(), name="provider_update"),
    path("provider/delete/<int:pk>", views.ProviderDeleteView.as_view(), name="provider_delete"),
    path("patient/create", views.PatientCreateView.as_view(), name="patient_create"),
    path("patient/update/<int:pk>", views.PatientUpdateView.as_view(), name="patient_update"),
    path("patient/delete/<int:pk>", views.PatientDeleteView.as_view(), name="patient_delete"),
    path("appointment/create", views.AppointmentCreateView.as_view(), name="appointment_create"),
    path("appointment/update/<int:pk>", views.AppointmentUpdateView.as_view(), name="appointment_update"),
    path("appointment/delete/<int:pk>", views.AppointmentDeleteView.as_view(), name="appointment_delete")
]
