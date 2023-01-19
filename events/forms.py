from django import forms
from django.forms import ModelForm
from .models import Event


# Event Form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
