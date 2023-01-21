from django.shortcuts import render


def bag(request):
    """A view to return the shopping bag"""

    return render(request, 'bag/bag.html')
