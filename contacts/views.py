# contacts/views.py

from django.shortcuts import render
from contacts.models import Contact

def contact_index(request):
    contact = Contact.objects.all()
    context = {
        "contact": contact
    }
    return render(request, "contacts/contact_index.html", context)
