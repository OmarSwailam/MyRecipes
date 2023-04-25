from .common import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["myrecipes.herokuapp.com"]


DATABASES = {"default": dj_database_url.config()}


EMAIL_HOST = os.environ[""]
EMAIL_HOST_USER = os.environ[""]
EMAIL_HOST_PASSWORD = os.environ[""]
EMAIL_PORT = os.environ[""]
EMAIL_USE_TLS = True


SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
# to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True
# to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 86400 * 365
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
