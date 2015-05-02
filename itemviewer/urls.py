from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<summoner_id>[0-9]+)/$', views.summoner, name='summoner'),
    url(r'^match/(?P<match_id>[0-9]+)/$', views.match, name='match'),
]
