from django.urls import path

from . import views

urlpatterns = [
    path("", views.ServMonView.as_view(), name=""),
    path("create/", views.ServCreateView.as_view()),
]
