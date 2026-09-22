"""
Django settings for the Muhammad Nouman portfolio project.
"""

from pathlib import Path
import os

from decouple import config, Csv


# ------------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / "subdir".
# ------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------------------------------------------------
# Core / Security
# ------------------------------------------------------------------

SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-change-this-key-in-production",
)

DEBUG = config(
    "DEBUG",
    default=True,
    cast=bool,
)


# ------------------------------------------------------------------
# Allowed Hosts
# ------------------------------------------------------------------

# Local development hosts
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Optional hosts from .env / Render environment
extra_allowed_hosts = config(
    "ALLOWED_HOSTS",
    default="",
    cast=Csv(),
)

for host in extra_allowed_hosts:
    host = host.strip()
    if host and host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(host)


# Render automatically provides this variable
render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if render_hostname:
    render_hostname = render_hostname.strip()

    if render_hostname and render_hostname not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(render_hostname)


# ------------------------------------------------------------------
# CSRF Trusted Origins
# ------------------------------------------------------------------

CSRF_TRUSTED_ORIGINS = []

# Values manually provided through environment
extra_csrf_origins = config(
    "CSRF_TRUSTED_ORIGINS",
    default="",
    cast=Csv(),
)

for origin in extra_csrf_origins:
    origin = origin.strip()

    if origin and origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)


# Render automatically provides the public URL
render_url = os.environ.get("RENDER_EXTERNAL_URL")

if render_url:
    render_url = render_url.strip()

    if render_url and render_url not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(render_url)

elif render_hostname:
    render_origin = f"https://{render_hostname}"

    if render_origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(render_origin)


# ------------------------------------------------------------------
# Site
# ------------------------------------------------------------------

SITE_NAME = config(
    "SITE_NAME",
    default="Muhammad Nouman",
)


# ------------------------------------------------------------------
# Applications
# ------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps
    "apps.home",
    "apps.about",
    "apps.experience",
    "apps.projects",
    "apps.services",
    "apps.skills",
    "apps.contact",
]


# ------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise for serving static files in production
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ------------------------------------------------------------------
# URLs / WSGI / ASGI
# ------------------------------------------------------------------

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

ASGI_APPLICATION = "core.asgi.application"


# ------------------------------------------------------------------
# Templates
# ------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_meta",
            ],
        },
    },
]


# ------------------------------------------------------------------
# Database
# ------------------------------------------------------------------

_db_engine = config(
    "DB_ENGINE",
    default="django.db.backends.sqlite3",
)


if "sqlite3" in _db_engine:

    DATABASES = {
        "default": {
            "ENGINE": _db_engine,
            "NAME": BASE_DIR / config(
                "DB_NAME",
                default="db.sqlite3",
            ),
        }
    }

else:

    DATABASES = {
        "default": {
            "ENGINE": _db_engine,

            "NAME": config(
                "DB_NAME",
                default="nouman_portfolio",
            ),

            "USER": config(
                "DB_USER",
                default="postgres",
            ),

            "PASSWORD": config(
                "DB_PASSWORD",
                default="",
            ),

            "HOST": config(
                "DB_HOST",
                default="127.0.0.1",
            ),

            "PORT": config(
                "DB_PORT",
                default="5432",
            ),
        }
    }


# ------------------------------------------------------------------
# Password validation
# ------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# ------------------------------------------------------------------
# Internationalization
# ------------------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = config(
    "TIME_ZONE",
    default="Asia/Karachi",
)

USE_I18N = True

USE_TZ = True


# ------------------------------------------------------------------
# Static & Media Files
# ------------------------------------------------------------------

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ------------------------------------------------------------------
# WhiteNoise Static File Storage
# ------------------------------------------------------------------

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },

    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage"
        ),
    },
}


# ------------------------------------------------------------------
# Production Security
# ------------------------------------------------------------------

if not DEBUG:

    # Render terminates HTTPS at its proxy.
    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True


# ------------------------------------------------------------------
# Default Primary Key
# ------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ------------------------------------------------------------------
# Contact Form / Site Owner Information
# ------------------------------------------------------------------

OWNER_NAME = config(
    "OWNER_NAME",
    default="Muhammad Nouman",
)

OWNER_EMAIL = config(
    "OWNER_EMAIL",
    default="nomannisar769@gmail.com",
)

OWNER_PHONE = config(
    "OWNER_PHONE",
    default="0324 8699647",
)

OWNER_LOCATION = config(
    "OWNER_LOCATION",
    default="Farooqabad District, Sheikhupura",
)

OWNER_GITHUB = config(
    "OWNER_GITHUB",
    default="https://github.com/MuhammadNouman769",
)

OWNER_LINKEDIN = config(
    "OWNER_LINKEDIN",
    default="https://www.linkedin.com/in/muhammad-nouman-524ab9360/",
)