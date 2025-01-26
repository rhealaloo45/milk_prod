from django.urls import path
from . import views

urlpatterns = [
    path("", views.predict_milk_production, name="predict_milk"),
    path("result/", views.result, name="result"),
]
