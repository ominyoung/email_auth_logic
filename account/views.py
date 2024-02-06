import string
import random

import pyotp
from django.http import HttpResponse
from django.core.mail import send_mail

from EmailAuthLogic import settings


def send_welcome_email(request, email):
    send_mail(
        'Welcome to our website',
        'Thank you for registering for our website. We hope you enjoy our service \n',
        settings.EMAIL_HOST_USER,
        ['ohmj090747@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent')

