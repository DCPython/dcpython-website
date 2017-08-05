# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html', {})

def code_of_conduct(request):
    return render(request, 'code-of-conduct.html', {})

def home(request):
    return render(request, 'home.html', {})

def team(request):
    return render(request, 'team.html', {})

