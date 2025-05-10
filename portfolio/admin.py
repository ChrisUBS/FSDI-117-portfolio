from django.contrib import admin
from .models import skill, project, timelineEntry

# Register your models here.
admin.site.register(skill)
admin.site.register(project)
admin.site.register(timelineEntry)