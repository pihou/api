# -*- coding: utf-8 -*-
from rest_framework.views import APIView as BaseAPIView
from rest_framework.exceptions import APIException, ParseError, UnsupportedMediaType
from rest_framework.response import Response
from pprint import pprint
from django.conf import settings
from redis import Redis

import simplejson as json
import time
import exception
import logging

logger_error = logging.getLogger('error')
logger_access = logging.getLogger('access')
NO_DATA_EXCEPTION = set([ParseError, UnsupportedMediaType])


"""
check_throttles使用rest_framework自带
"""

#---------------------------------------------------------------------
def check_auth(position):
    def outer(func):
        def inner(views, request, *args, **kwargs):
            return func(views, request, *args, **kwargs)
        return inner
    return outer


def check_time(position):
    def outer(func):
        def wrap(views, request, *args, **kwargs):
            return func(views, request, *args, **kwargs)
        return wrap
    return outer

#---------------------------------------------------------------------
def valid_param(serial, data):
    def outer(func):
        def wrap(views, request, *args, **kwargs):
            ret = func(views, request, *args, **kwargs)
            return ret
        return wrap
    return outer


def valid_version(func):
    def wrap(views, request, *args, **kwargs):
        return func(views, request, *args, **kwargs)
    return wrap

#---------------------------------------------------------------------

class APIView(BaseAPIView):
    def handle_exception(self, exc):
        ret = super(APIView, self).handle_exception(exc)
        ret.exc_class = exc.__class__
        return ret

    def dispatch(self, request, *args, **kwargs):
        ret = super(APIView, self).dispatch(request, *args, **kwargs)
        request = self.request
        if ret.exception and ret.exc_class in NO_DATA_EXCEPTION:
            data = None
        elif request.content_type.startswith("application/json"):
            data = request.data
        else:
            data = None

        access = "method:%s, path:%s, token:%s, query_params:%s, content_type:%s, data:%s, ret:%s"%(
            request.method,
            request.path,
            request.META.get("HTTP_AUTH_TOKEN"),
            request.query_params,
            request.content_type,
            data,
            getattr(ret, "data", None)
        )
        #logger_access.info(access)
        return ret

