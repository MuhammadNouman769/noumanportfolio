from django.shortcuts import render

from apps.experience.models import Experience
from apps.projects.models import Project
from apps.skills.models import SkillCategory, Skill
from apps.services.models import Service


def home(request):
    """Landing page: hero + a quick taste of experience, projects, skills, services."""
    context = {
        'experiences': Experience.objects.all()[:2],
        'projects': Project.objects.filter(featured=True).prefetch_related('tags')[:3],
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all()[:3],
        'services': Service.objects.all()[:8],

        # Hero stat bar — real counts pulled straight from the database.
        'projects_count': Project.objects.count(),
        'services_count': Service.objects.count(),
        'skills_count': Skill.objects.count(),
        'live_projects_count': Project.objects.filter(status=Project.STATUS_LIVE).count(),
    }
    return render(request, 'home/home.html', context)