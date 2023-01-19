from django.shortcuts import render
from .models import Activity, Event
from django.views.generic import ListView


# Event View
class EventList(ListView):
    """Create Route View"""
    model = Event
    queryset = Event.objects.filter(published_status=1).order_by('date')
    template_name = 'events/events.html'


# Admin Panel
def admin_panel(request):
    """Superuser can view all events on the database from the frontend"""

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        events = Event.objects.all()

        context = {
                'events': events,
                }

        return render(request, 'events/admin_panel.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')
