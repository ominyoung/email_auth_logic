from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from EmailAuthLogic import settings


def send_welcome_email(request):
    send_mail(
        'Welcome to our website',
        'Thank you for registering for our website. We hope you enjoy our service',
        settings.EMAIL_HOST_USER,
        # [request.user.email],
        ['ohmj090747@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent')