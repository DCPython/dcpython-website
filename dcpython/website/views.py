# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from faker import Faker
from django.shortcuts import render
from django.conf import settings
import requests

fake = Faker()


def get_fake_text(num):
    items = []
    for _ in range(0, 20):
        items.append(fake.text())
    return items


def get_events():
    """
    """
    url = '/'.join([settings.MEETUP_API_URL, 'dcpython', 'events?sign=True'])
    response = requests.get(url)
    events = []
    for event in response.json():
        if not event['name'].startswith('[pending'):  # filter out pending
            events.append(event)
    return events


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
    # events = get_fake_text(20)
    events = get_events()
    context['events'] = events
    return render(request, 'home.html', context)


def legal(request):
    return render(request, 'legal.html', {})


def team(request):
    context = {}
    organizers = get_fake_text(20)
    context['organizers'] = organizers
    return render(request, 'team.html', context)


def sponsors(request):
    return render(request, 'sponsors.html', {})
