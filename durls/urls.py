from django.urls import path
from durls.views import HomeView, DestinationListView, redirect_view

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("+/", DestinationListView.as_view(), name="manage"),
    path("<slug>/", redirect_view, name="redirect"),
]
