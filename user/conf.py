from appconf import AppConf
from django.conf import settings


class UserAppConf(AppConf):
    REGISTRATION_OPEN = True
    AUTO_LOGIN_ON_ACTIVATION = True
    AUTO_LOGIN_AFTER_REGISTRATION = False
    PASSWORD_MIN_LENGTH = 5
    PASSWORD_MAX_LENGTH = None
    CHECK_PASSWORD_COMPLEXITY = True
    PASSWORD_POLICY = {
        'UPPER': 0,       # Uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'LOWER': 0,       # Lowercase 'abcdefghijklmnopqrstuvwxyz'
        'DIGITS': 0,      # Digits '0123456789'
        'PUNCTUATION': 0  # Punctuation """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    }

    class Meta:
        prefix = 'user'
