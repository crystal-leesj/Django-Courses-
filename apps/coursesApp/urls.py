from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^course/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^remove_course/(?P<id>\d+)$', views.remove_course),
]
