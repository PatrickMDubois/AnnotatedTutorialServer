from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tutorials$', views.tutorials),
    url(r'^tutorials/(?P<tutorial_id>[0-9]+)$', views.tutorial),
    url(r'^author/(?P<author_name>[a-zA-Z]+)$', views.author),
    url(r'^notes$', views.notes),
    url(r'^note/update/(?P<note_id>[a-zA-Z0-9]+)$', views.change_note),
]
