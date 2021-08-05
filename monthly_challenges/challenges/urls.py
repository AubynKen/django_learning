from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="month-challenge-index"),
    path("<int:month>", views.monthly_challenge_numeric),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
