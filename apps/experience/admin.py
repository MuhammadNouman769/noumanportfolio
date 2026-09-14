from django.contrib import admin
from .models import Experience, ExperienceHighlight


class ExperienceHighlightInline(admin.TabularInline):
    model = ExperienceHighlight
    extra = 1


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'date_range', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    inlines = [ExperienceHighlightInline]
