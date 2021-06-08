import logging

from .compat import dictConfig


# Taken from https://github.com/nvie/rq/blob/master/rq/logutils.py
def setup_loghandlers(level=None):
    # Setup logging for post_nord if not already configured
    logger = logging.getLogger("post_nord")
    if not logger.handlers:
        dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    "post_nord": {
                        "format": "[%(levelname)s]%(asctime)s PID %(process)d: %(message)s",
                        "datefmt": "%Y-%m-%d %H:%M:%S",
                    }
                },
                "handlers": {
                    "post_nord": {
                        "level": "DEBUG",
                        "class": "logging.StreamHandler",
                        "formatter": "post_nord",
                    }
                },
                "loggers": {
                    "post_nord": {"handlers": ["post_nord"], "level": level or "DEBUG"}
                },
            }
        )
    return logger
