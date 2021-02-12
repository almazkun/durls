from django.urls import path, include
from durls.views import DestinationCreateView, redirector

urlpatterns = [
    path("_/", DestinationCreateView.as_view(), name="destination_list"),
    path("<slug>", redirector, name="redirector"),
]
