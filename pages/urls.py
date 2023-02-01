# This file was created and not added by the boilerplate
from django.urls import path
from .views import homePageView


urlpatterns = [
    path("", homePageView, name="home"),
]
