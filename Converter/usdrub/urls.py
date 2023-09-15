from django.urls import path
from . import views


urlpatterns = [
    path("api/rates/", views.convert_currency, name="convert_currency"),
]