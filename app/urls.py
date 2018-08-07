# usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.db import transaction

import views

urlpatterns = [
    url(r'^benchmark/$', views.BenchMarkView.as_view(), name="benchmark"),
]

