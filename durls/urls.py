from django.urls import path, include
from durls.views import DestinationListView

urlpatterns = [
    path("", DestinationListView.as_view(), name="destination_list"),
]
