# This file contains the WSGI configuration required to serve up your
# web application at http://facebookuser043.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys

import requests

response = requests.post("https://tudynotification.app.n8n.cloud/webhook/64e9e6b2-0695-415a-a82e-9e498942915f", json={
    "userId": 1,
    "title": "Online Script is Working",
    "completed": False
}, headers={
    "Content-type": "application/json; charset=UTF-8"
})

# add your project directory to the sys.path
project_home = '/home/facebookuser043/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

