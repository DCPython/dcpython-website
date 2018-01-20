"""dcpython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .website import views

urlpatterns = [
    url(r'^make_donation$', views.make_donation),
    url(r'^about$', views.about, name='about'),
    url(r'^andrew-w-singer$', views.andrew_w_singer, name='andrew-w-singer'),
    url(r'^code-of-conduct$', views.code_of_conduct, name='code-of-conduct'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^donate$', views.donate, name='donate'),
    url(r'^legal$', views.legal, name='legal'),
    url(r'^sponsors$', views.sponsors, name='sponsors'),
    url(r'^team$', views.team, name='team'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
]
