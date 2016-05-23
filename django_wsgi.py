#!/usr/bin/env python
# conding: utf-8

import os
import sys

from django.core.wsgi import get_wsgi_application
import open_source as application

reload(sys)
# reload(__import__('sys')).setdefaultencoding('utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "open_source.settings")

# application = get_wsgi_application()
application = application
