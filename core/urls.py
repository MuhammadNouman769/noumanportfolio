from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('about/', include('apps.about.urls')),
    path('experience/', include('apps.experience.urls')),
    path('projects/', include('apps.projects.urls')),
    path('services/', include('apps.services.urls')),
    path('skills/', include('apps.skills.urls')),
    path('contact/', include('apps.contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
