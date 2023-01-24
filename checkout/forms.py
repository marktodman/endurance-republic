from django import forms
from .models import Order


# Code edited from Code Institute Boutique Ado Walkthrough
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name','email', 'phone_number',
                'emergency_contact', 'emergency_number', 'medical',
                'street_address1', 'street_address2',
                'town_or_city', 'county', 'country', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postal Code',
            'emergency_contact': 'Emergency Contact',
            'emergency_number': 'Emergency Contact Phone Number',
            'medical': 'Medical Information - confirm None or add details',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
