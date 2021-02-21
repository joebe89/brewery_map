"""Markers urls."""

from django.urls import path

from .views import BrewMapView

app_name = "brew_base"

urlpatterns = [
    path("map/", BrewMapView.as_view()),
]
