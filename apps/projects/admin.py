from django.contrib import admin
from .models import Project, ProjectTag, ProjectFeature

class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'featured', 'order')
    list_editable = ('featured', 'order')
    list_filter = ('status', 'featured')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectTagInline, ProjectFeatureInline]