# -*- coding: utf-8 -*-
from django.utils import timezone
from django.core.urlresolvers import reverse
from api.base import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from redis import Redis
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from pprint import pprint
from django.db.models import F

import simplejson as json
import uuid
import time
import random
import urllib

class BenchMarkView(APIView):

    def get(self, request, *args, **kwargs):
        info = {
            "ret_code": 0,
            "ret_msg": "",
        }
        return Response(info)

