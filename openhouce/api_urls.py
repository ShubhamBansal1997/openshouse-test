# Third Party Stuff
from rest_framework.routers import DefaultRouter

# openhouce Stuff
from openhouce.base.api.routers import SingletonRouter
from openhouce.users.api import CurrentUserViewSet
from openhouce.users.auth.api import AuthViewSet
from openhouce.urlshotener.api import ShortURLViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register("auth", AuthViewSet, basename="auth")
singleton_router.register("me", CurrentUserViewSet, basename="me")
default_router.register("short_url", ShortURLViewSet, basename="short_url")

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
