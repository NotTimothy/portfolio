# pages/models.py

from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    image = models.FileField(upload_to="project_images/", blank=True)
    github = models.CharField(max_length=200)
    website = models.CharField(max_length=200)