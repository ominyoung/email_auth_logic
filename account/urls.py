from django.urls import path
from account.views import send_welcome_email

app_name = 'account'

urlpatterns = [
    path('send_welcome_email/', send_welcome_email, name='send_welcome_email'),
]