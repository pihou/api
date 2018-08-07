# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.exceptions import APIException

import time

class TimestampError(APIException):
    pass

class AuthTokenError(APIException):
    pass

class ParameterError(APIException):
    pass

class CaptchaError(APIException):
    pass

class VersionError(APIException):
    pass

class NetworkError(APIException):
    pass

class PasswordError(APIException):
    pass

class AccountError(APIException):
    pass

class PasscodeError(APIException):
    pass

class BindingError(APIException):
    pass

class PermissionError(APIException):
    pass

class NotFoundError(APIException):
    pass

class CapacityError(APIException):
    pass

class ThirdPartyError(APIException):
    pass

class ServerCapacityError(APIException):
    pass

class OwnerTransferError(APIException):
    pass

class CreateBindingError(APIException):
    pass

