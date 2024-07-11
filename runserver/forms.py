from django import forms
from runserver.models import appointment

class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['name', 'email', 'phone', 'date', 'department','doctor','message']