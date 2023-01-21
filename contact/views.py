from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm


def contact(request):
    """User can submitted a contact form"""

    submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (
                'Success! Your contact request has been sent. \
                    We will get back to you soon!'))
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
        }

    return render(request, 'contact/contact.html', context)
