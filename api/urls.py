# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    url(r'^app/', include('app.urls', namespace="app")),
]

