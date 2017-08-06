# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def about(request):
    context = {}
    context['active_nav'] = 'active'
    return render(request, 'about.html', context)

def andrew_w_singer(request):
    return render(request, 'andrew-w-singer.html', {})

def code_of_conduct(request):
    return render(request, 'code-of-conduct.html', {})

def donate(request):
    return render(request, 'donate.html', {})

def home(request):
    context = {}
    return render(request, 'home.html', {})

def team(request):
    return render(request, 'team.html', {})

