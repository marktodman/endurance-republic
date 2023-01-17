from django.shortcuts import render
from .models import Activity, Event
from django.views.generic import ListView


# Event View
class EventList(ListView):
    """Create Route View"""
    model = Event
    queryset = Event.objects.filter(published_status=1).order_by('date')
    template_name = 'events/events.html'
