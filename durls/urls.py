from django.urls import path
from durls.views import (
    HomeView,
    DestinationCreateView,
    DestinationDeleteView,
    redirect_view,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("+/", DestinationCreateView.as_view(), name="create"),
    path("+/delete/<slug>/", DestinationDeleteView.as_view(), name="delete"),
    path("<slug>/", redirect_view, name="redirect"),
]
