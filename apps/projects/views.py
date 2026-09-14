from django.shortcuts import render
from .models import Project


def projects(request):
    context = {
        'projects': Project.objects.prefetch_related('tags').all(),
    }
    return render(request, 'projects/projects.html', context)
