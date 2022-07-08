from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nikita", views.nikita, name="nikita"),
    path("<str:name>", views.greet, name="greet"),
]