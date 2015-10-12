from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/getWorldToCreate$', views.getWorldToCreate, name='getWorldToCreate'),
    url(r'^api/submitWorld$', views.submitWorld, name='submitWorld'),
    url(r'^$', views.index, name='index'),
]