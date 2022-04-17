from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime, timezone


def is_dark_mode_processor(request):
    dark_mode = True if request.COOKIES.get('dark-mode', None) == 'true' else False
    return {'dark_mode': dark_mode}


def home(request):
    return render(request, 'index.html', is_dark_mode_processor(request))


def toggle_dark_mode(request):
    dark_mode = 'true' if request.COOKIES.get('dark-mode', 'false') == 'false' else 'false'
    expires = datetime(2048, 12, 31, tzinfo=timezone.utc)

    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie('dark-mode', dark_mode, expires=expires, httponly=True, secure=True)
    return response

