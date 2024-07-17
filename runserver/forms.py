from django import forms
from runserver.models import appointment,ImageModel

class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['name', 'email', 'phone', 'date', 'department','doctor','message']




class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']