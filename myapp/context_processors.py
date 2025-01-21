# myapp/context_processors.py

from django.conf import settings

def debug(request):
    return {'debug': settings.DEBUG}