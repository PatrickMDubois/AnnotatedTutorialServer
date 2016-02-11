from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tutorial$', views.tutorial),
]