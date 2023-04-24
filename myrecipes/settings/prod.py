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
