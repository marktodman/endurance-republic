from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


# Modified from Code Institute Boutique Ado Walkthrough
def bag(request):
    """A view to return the shopping bag"""

    return render(request, 'bag/bag.html')


# Modified from Code Institute Boutique Ado Walkthrough
def add_to_bag(request, event_id):
    """ Add an Event to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if event_id in list(bag.keys()):
        messages.success(request, (
            'Sorry, you cannot book more than one place \
                on each event! Contact us and we will help arrange your \
                    booking.'))
    else:
        bag[event_id] = quantity
        messages.success(request, (
                    'Success! Your event has been added to your cart'))

    request.session['bag'] = bag

    return redirect(redirect_url)


# Modified from Code Institute Boutique Ado Walkthrough
def remove_from_bag(request, event_id):
    """Remove the event from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(event_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
