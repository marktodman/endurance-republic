from django import forms
from django.forms import ModelForm
from .models import Contact


# Event Form
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
