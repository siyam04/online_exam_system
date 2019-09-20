import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from custom_users.models import Profile


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = ''

    template = 'home.html'
    context = {'profile': profile}

    return render(request, template, context)

