# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book$',views.bookApi),
    url(r'^book/([0-9]+)$',views.bookApi),
    url(r'^Book/saveImage$', views.saveImage),
    url(r'^review$',views.reviewApi),
    url(r'^review/([0-9]+)$',views.reviewApi),
]