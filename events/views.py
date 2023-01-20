from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Activity, Event
from django.views.generic import ListView
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


# Edit Event
@login_required
def edit_event(request, event_id):
    """Superuser can edit eventss on the database from the frontend"""

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        event = Event.objects.get(id=event_id)

        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES, instance=event)

            if form.is_valid():
                form.save()
                messages.success(request, (
                    'Success! Your changes have been saved to the database'))
                return redirect('admin-panel')

        form = EventForm(instance=event)
        context = {
            'event': event,
            'form': form,
            }

        return render(request, 'events/edit_event.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Add Event
@login_required
def add_event(request):
    """Superuser can add an event to the database from the frontend"""

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        submitted = False

        if request.method == "POST":
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, (
                    'Success! The event has been added to the database'))
                return HttpResponseRedirect('?submitted=True')
        else:
            form = EventForm
            if 'submitted' in request.GET:
                submitted = True

        context = {
            'form': form,
            'submitted': submitted
            }

        return render(request, 'events/add_event.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Delete Event
@login_required
def delete_event(request, event_id):
    """Superuser can delete an Event"""

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        event = Event.objects.get(id=event_id)

        # Check that user really wants to delete this route
        if request.method == 'POST':
            event.delete()
            messages.success(request, (
                'Success! The event has been deleted from the database'))
            return redirect('admin-panel')

        context = {
                'event': event
                }

        return render(request, 'events/delete_event.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')
