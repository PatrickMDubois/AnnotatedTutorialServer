from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tutorials$', views.tutorials),
    url(r'^tutorials/(?P<tutorial_id>[0-9]+)$', views.tutorial),
]
