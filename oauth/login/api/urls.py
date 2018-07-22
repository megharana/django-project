from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from .views import(
	PostListAPIView
	)
# from social_django.urls import extra
# from login.views import complete


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
]