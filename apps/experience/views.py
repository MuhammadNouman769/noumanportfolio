from django.shortcuts import render
from .models import Experience


def experience(request):
    context = {
        'experiences': Experience.objects.prefetch_related('highlights').all(),
    }
    return render(request, 'experience/experience.html', context)
