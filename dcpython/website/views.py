# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from faker import Faker
from django.shortcuts import render

def get_fake_text(num):
    fake = Faker()
    items = []
    for _ in range(0, 20):
        items.append(fake.text())
    return items

# Create your views here.


def about(request):
    context = {}
    context['active_nav'] = 'active'
    return render(request, 'about.html', context)


def andrew_w_singer(request):
    return render(request, 'andrew-w-singer.html', {})


def code_of_conduct(request):
    return render(request, 'code-of-conduct.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def donate(request):
    return render(request, 'donate.html', {})


def home(request):
    context = {}
    events = get_fake_text(20)
    context['events'] = events
    return render(request, 'home.html', context)


def legal(request):
    return render(request, 'legal.html', {})


def team(request):
    context = {}
    organizers = get_fake_text(20)
    context['organizers'] = organizers
    return render(request, 'team.html', context)
