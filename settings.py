import warnings

from django.conf import settings
from django.core.cache.backends.base import InvalidCacheBackendError

from .compat import import_attribute, get_cache


def get_backend(alias="default"):
    return get_available_backends()[alias]


def get_available_backends():
    """ Returns a dictionary of defined backend classes. For example:
    {
        'default': 'django.core.mail.backends.smtp.EmailBackend',
        'locmem': 'django.core.mail.backends.locmem.EmailBackend',
    }
    """
    backends = get_config().get("BACKENDS", {})

    if backends:
        return backends

    # Try to get backend settings from old style
    # POST_NORD = {
    #     'EMAIL_BACKEND': 'mybackend'
    # }
    backend = get_config().get("EMAIL_BACKEND")
    if backend:
        warnings.warn(
            'Please use the new POST_NORD["BACKENDS"] settings', DeprecationWarning
        )

        backends["default"] = backend
        return backends

    # Fall back to Django's EMAIL_BACKEND definition
    backends["default"] = getattr(
        settings, "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
    )

    # If EMAIL_BACKEND is set to use PostNordBackend
    # and POST_NORD_BACKEND is not set, fall back to SMTP
    if "post_nord.EmailBackend" in backends["default"]:
        backends["default"] = "django.core.mail.backends.smtp.EmailBackend"

    return backends


def get_cache_backend():
    if hasattr(settings, "CACHES"):
        if "post_nord" in settings.CACHES:
            return get_cache("post_nord")
        else:
            # Sometimes this raises InvalidCacheBackendError, which is ok too
            try:
                return get_cache("default")
            except InvalidCacheBackendError:
                pass
    return None


def get_config():
    """
    Returns Post Nord's configuration in dictionary format. e.g:
    POST_NORD = {
        'BATCH_SIZE': 1000
    }
    """
    return getattr(settings, "POST_NORD", {})


def get_batch_size():
    return get_config().get("BATCH_SIZE", 100)


def get_threads_per_process():
    return get_config().get("THREADS_PER_PROCESS", 5)


def get_default_priority():
    return get_config().get("DEFAULT_PRIORITY", "medium")


def get_log_level():
    return get_config().get("LOG_LEVEL", 2)


def get_sending_order():
    return get_config().get("SENDING_ORDER", ["-priority"])


CONTEXT_FIELD_CLASS = get_config().get("CONTEXT_FIELD_CLASS", "jsonfield.JSONField")
context_field_class = import_attribute(CONTEXT_FIELD_CLASS)
