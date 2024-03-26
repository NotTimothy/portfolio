# projects/views.py

from django.shortcuts import render
from pages.models import Page

def home(request):
    pages = Page.objects.all()
    context = {
        "pages": pages
    }
    
    return render(request, "pages/home.html", context)