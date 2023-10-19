from django.urls import path
from Backend import views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("Products/", views.ProductsList)
]