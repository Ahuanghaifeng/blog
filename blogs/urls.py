
from django.conf.urls import url
from . import views

urlpatterns = [
    # ^$约束空字符串 ^index/$分号很重要
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page),
]
