# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from faker import Faker
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils import timezone
from json.decoder import JSONDecodeError
import requests

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import json
import stripe


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
            ms = event['time']
            when = timezone.datetime.fromtimestamp(ms/1000.0)
            event['when'] = when
            events.append(event)
    return events[:3]  # Display first 3 events


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


@cache_page(300)
def home(request):
    context = {}
    try:
        events = get_events()
        context['events'] = events
    except JSONDecodeError:
        pass
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


def make_donation(request):
    """
    this method is called via ajax by the donate page.
    if form is invalid, returns form containing error messages else,
    makes debit and redirects.
    """
    if request.method != 'POST':
        return HttpResponse(json.dumps({"error": "only POST supported"}))

    donation_data = dict(request.POST)
    donation_amount = donation_data["donation"]

    # Create the charge on Stripe's servers - this will charge the user's
    # card
    try:
        resp = stripe.Charge.create(
            amount=donation_amount*100,  # amount in cents, again
            currency="usd",
            card=donation_data['cc_token']
        )
    except stripe.CardError as e:
        resp = {"payment_error": str(e)}
        return HttpResponse(json.dumps(resp))

    return HttpResponse(json.dumps(resp))
