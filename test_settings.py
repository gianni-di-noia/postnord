# -*- coding: utf-8 -*-


import django
from distutils.version import StrictVersion

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

# Default values: True
# POST_NORD_CACHE = True
# POST_NORD_TEMPLATE_CACHE = True


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 36000,
        "KEY_PREFIX": "post-nord",
    },
    "post_nord": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 36000,
        "KEY_PREFIX": "post-nord",
    },
}

POST_NORD = {
    "BACKENDS": {
        "default": "django.core.mail.backends.dummy.EmailBackend",
        "locmem": "django.core.mail.backends.locmem.EmailBackend",
        "error": "post_nord.tests.test_backends.ErrorRaisingBackend",
        "smtp": "django.core.mail.backends.smtp.EmailBackend",
        "connection_tester": "post_nord.tests.test_mail.ConnectionTestingBackend",
    }
}


INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "post_nord",
)

SECRET_KEY = "a"

ROOT_URLCONF = "post_nord.test_urls"

DEFAULT_FROM_EMAIL = "webmaster@example.com"

if StrictVersion(str(django.get_version())) < "1.10":
    MIDDLEWARE_CLASSES = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
    )
else:
    MIDDLEWARE = [
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
    ]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
