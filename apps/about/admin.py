from django.contrib import admin
from .models import Profile, Education


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('headline',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'date_range', 'order')
    list_editable = ('order',)
    ordering = ('order',)
