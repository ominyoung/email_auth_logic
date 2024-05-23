from django.http import HttpResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

from EmailAuthLogic import settings
from account.models import MyUser
from account.serializers import ProfileSerializer


def send_welcome_email(request, email):
    send_mail(
        'Welcome to our website',
        'Thank you for registering for our website. We hope you enjoy our service \n',
        settings.EMAIL_HOST_USER,
        ['ohmj090747@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent')


@api_view(['GET'])
def profile_thumbnail(request, *args, **kwargs):
    profile_id = kwargs['profile_id']

    user_profile = MyUser.objects.get(id=profile_id)
    serializer = ProfileSerializer(user_profile, context={'request': request})
    return Response(serializer.data)