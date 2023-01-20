from django import forms
from django.forms import ModelForm
from .models import Event


# Event Form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
                }
