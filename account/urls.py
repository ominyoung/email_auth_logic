from django.urls import path
from account.views import send_welcome_email, profile_thumbnail

app_name = 'account'

urlpatterns = [
    path('send_welcome_email/', send_welcome_email, name='send_welcome_email'),
    path('profile/<int:profile_id>/thumbnail/', profile_thumbnail, name='profile_thumbnail')
]