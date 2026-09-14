from django.conf import settings


def site_meta(request):
    """Make owner/site details available in every template without
    having to pass them from each view."""
    return {
        'SITE_NAME': settings.SITE_NAME,
        'OWNER_NAME': settings.OWNER_NAME,
        'OWNER_EMAIL': settings.OWNER_EMAIL,
        'OWNER_PHONE': settings.OWNER_PHONE,
        'OWNER_LOCATION': settings.OWNER_LOCATION,
        'OWNER_GITHUB': settings.OWNER_GITHUB,
        'OWNER_LINKEDIN': settings.OWNER_LINKEDIN,
    }
