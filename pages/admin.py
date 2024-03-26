# projects/admin.py

from django.contrib import admin
from pages.models import Page

class HomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, HomeAdmin)