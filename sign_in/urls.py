from django.urls import path

from sign_in.views import signed_up
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.verify, name='verify'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('signedup/', signed_up.as_view(), name='signed_up'),
    path('test/post', csrf_exempt(views.test_post), name='test-post')
]
