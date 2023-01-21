from django.shortcuts import render, redirect


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
        bag[event_id] += quantity
    else:
        bag[event_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
