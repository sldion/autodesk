import logging
import os
from logging.config import dictConfig


from logging.config import dictConfig

# set loggin level when debug_mode is activate
if os.getenv("DEBUG_MODE", False):
    level = "DEBUG"
else:
    level = "ERROR"

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": level, "handlers": ["wsgi"]},
    }
)

# disable the built in logging because of section 2
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

# from flask import has_request_context, request
# from flask.logging import default_handler


# class RequestFormatter(logging.Formatter):
#     def format(self, record):
#         if has_request_context():
#             record.url = request.url
#             record.remote_addr = request.remote_addr
#         else:
#             record.url = None
#             record.remote_addr = None

#         return super().format(record)


# formatter = RequestFormatter(
#     "[%(asctime)s] %(remote_addr)s requested %(url)s\n"
#     "%(levelname)s in %(module)s: %(message)s"
# )
# default_handler.setFormatter(formatter)
