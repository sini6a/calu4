from django.contrib import admin

# Register your models here.
from .models import Project, Donation

admin.site.register(Project)
admin.site.register(Donation)
