from django.shortcuts import render
from .models import Profile, Education


def about(request):
    context = {
        'profile': Profile.objects.first(),
        'education': Education.objects.all(),
    }
    return render(request, 'about/about.html', context)
