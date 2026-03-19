from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import AppointmentForm, PatientForm, ProviderForm
from .models import Appointment, Patient, Provider



class IndexView(ListView):
    model = Appointment
    template_name = "schedule/index.html"


class ProviderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    success_message = "Perfil de especialista registrado exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"

    def form_invalid(self, form):
        message = "Error: los datos ingresados no son válidos."
        messages.error(self.request, message)   
        return super().form_invalid(form)


class ProviderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Provider
    form_class = ProviderForm
    success_message = "Perfil de especialista editado exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"

    def form_invalid(self, form):
        message = "Error: los datos ingresados no son válidos."
        messages.error(self.request, message)
        return super().form_invalid(form)


class ProviderDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Provider
    success_message = "Perfil de especialista eliminado exitosamente."
    success_url = reverse_lazy("schedule:index")


class PatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    form_class = PatientForm
    success_message = "Perfil de paciente registrado exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"

    def form_invalid(self, form):
        message = "Error: los datos ingresados no son válidos."
        messages.error(self.request, message)
        return super().form_invalid(form)


class PatientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    success_message = "Perfil de paciente editado exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"

    def form_invalid(self, form):
        message = "Error: los datos ingresados no son válidos."
        messages.error(self.request, message)
        return super().form_invalid(form)


class PatientDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Patient
    success_message = "Perfil de paciente eliminado exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"


class AppointmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_message = "Hora agendada exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"

    def form_invalid(self, form):
        message = "Error: los datos ingresados no son válidos."
        messages.error(self.request, message)
        return super().form_invalid(form)


class AppointmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_message = "Hora reagendada exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"

    def form_invalid(self, form):
        message = "Error: los datos ingresados no son válidos."
        messages.error(self.request, message)
        return super().form_invalid(form)


class AppointmentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Appointment
    success_message = "Hora cancelada exitosamente."
    success_url = reverse_lazy("schedule:index")
    template_name = "schedule/crud.html"
