# contacts/urls.py

from django.urls import path
from contacts import views

urlpatterns = [
    path("", views.contact_index, name="contacts_index"),
]