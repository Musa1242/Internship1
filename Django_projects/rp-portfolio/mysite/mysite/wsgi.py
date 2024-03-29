"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

application = get_wsgi_application()


# from Contact_editor.wsgi import Contact_editorApplication
# application = Contact_editorApplication(application)
