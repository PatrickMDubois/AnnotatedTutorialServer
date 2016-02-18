from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tutorial/(?P<tutorial_id>[0-9]+)$', views.tutorial),
]
