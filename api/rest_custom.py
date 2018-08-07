# -*- coding: utf-8 -*-
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled, APIException, ParseError, UnsupportedMediaType
from rest_framework.response import Response

import logging
import exception

error_logger = logging.getLogger('error')
access_logger = logging.getLogger('access')

ERROR_INFO = {
    ParseError : {
        "ret_code": 1000,
        "ret_msg": 'http content error',
        "http_code": 200,
    },
    UnsupportedMediaType : {
        "ret_code": 1000,
        "ret_msg": 'media type error',
        "http_code": 200,
    },
    Throttled : {
        "ret_code": 1001,
        "ret_msg": 'request limit exceeded, available in some seconds',
        "http_code": 200,
    },
    exception.TimestampError : {
        "ret_code": 1002,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.AuthTokenError : {
        "ret_code": 1003,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.ParameterError : {
        "ret_code": 1004,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.CaptchaError : {
        "ret_code": 1005,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.NetworkError : {
        "ret_code": 1007,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.PermissionError : {
        "ret_code": 1008,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.NotFoundError : {
        "ret_code": 1009,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.ServerCapacityError : {
        "ret_code": 1010,
        "ret_msg": None,
        "http_code": 200,
    },
    #--------------------------
    # 2000 registered when register
    # 2001 not registered when login
    exception.AccountError : {
        "ret_code": None,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.PasswordError : {
        "ret_code": 2002,
        "ret_msg": None,
        "http_code": 200,
    },
    # 2003 binded when binding
    # 2004 not binded
    exception.BindingError : {
        "ret_code": None,
        "ret_msg": None,
        "http_code": 200,
    },
    # 2005 registered when register
    # 2006 not registered when login
    exception.PasscodeError : {
        "ret_code": None,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.CapacityError : {
        "ret_code": 2007,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.OwnerTransferError: {
        "ret_code": 2012,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.CreateBindingError:{
        "ret_code": 2012,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.VersionError : {
        "ret_code": 5000,
        "ret_msg": None,
        "http_code": 200,
    },
    exception.ThirdPartyError : {
        "ret_code": 8000,
        "ret_msg": None,
        "http_code": 200,
    },
}

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    request = context.get("request")
    custom_info = ERROR_INFO.get(exc.__class__)
    if custom_info:
        data = dict(custom_info)
        if not data["ret_msg"]:
            data["ret_msg"] = exc.detail
        ret_code = exc.get_codes()
        if isinstance(ret_code, int):
            data["ret_code"] = ret_code
        response.data = data
        response.status_code = data.pop("http_code", 200)
        return response

    data = {
        "ret_code": 9000,
        "ret_msg": "something wrong happened, not expected"
    }
    if not response:
        response = Response(data, status=500)
    else:
        response.data = data

    error_logger.exception(exc)
    return response

