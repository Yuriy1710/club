from django import forms
from django.forms import ModelForm
from .models import *

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        
        labels = {
            'name': "",
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email': '',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zipcode'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Web Address'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
        }
        
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        
        labels = {
            'name': "",
            'event_date': '',
            'venue': 'Venue',
            'manager': 'Manager',
            'description': '',
            'attendee': 'Attendee',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Manager'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Description'}),
            'attendee': forms.SelectMultiple(attrs={'class':'form-select', 'placeholder': 'Attendee'}),
        }