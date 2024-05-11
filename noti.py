# This file contains the WSGI configuration required to serve up your
# web application at http://facebookuser043.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys

import requests

response = requests.post("https://hook.eu2.make.com/2kyky66e8hfcitrge57je77xasyd6g7n", json={
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


