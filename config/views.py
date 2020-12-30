from django.shortcuts import render
from django.http import HttpResponseRedirect


def is_dark_mode_processor(request):
    dark_mode = True if request.COOKIES.get('dark-mode', None) == 'true' else False
    return {'dark_mode': dark_mode}


def home(request):
    return render(request, 'index.html', is_dark_mode_processor(request))


def toggle_dark_mode(request):
    dark_mode = 'true' if request.COOKIES.get('dark-mode', None) == 'false' else 'false'

    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie('dark-mode', dark_mode, httponly=True)
    return response

