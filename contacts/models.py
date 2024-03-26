# contacts/models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description = models.CharField(max_length=200)