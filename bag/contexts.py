from django.shortcuts import get_object_or_404
from events.models import Event


# Make available across all web app
def bag_contents(request):

    bag_items = []
    total = 0
    event_count = 0
    bag = request.session.get('bag', {})

    for event_id, quantity in bag.items():
        event = get_object_or_404(Event, pk=event_id)
        total += quantity * event.price
        event_count += quantity
        bag_items.append({
            'event_id': event_id,
            'quantity': quantity,
            'event': event,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'event_count': event_count,
    }

    return context
