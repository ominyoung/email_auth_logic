from django.urls import path

from start_celery import views

urlpatterns = [
    path('', views.test, name='test'),
]