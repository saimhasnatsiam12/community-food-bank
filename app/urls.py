
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("families/", views.families, name="families"),

    path("add-food/", views.add_food, name="add_food"),

    path("distribute/", views.distribute, name="distribute"),

    path("report/", views.report, name="report"),
]
