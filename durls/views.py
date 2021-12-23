from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from durls.models import Destination
from django.shortcuts import get_object_or_404
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy


class NoGetMixin:
    def get(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect(self.success_url)


class HomeView(TemplateView):
    template_name = "durls/home.html"


class DestinationListView(ListView):
    model = Destination
    template_name = "destination_list.html"
    context_object_name = "destinations"


class DestinationCreateView(NoGetMixin, CreateView):
    model = Destination
    success_url = reverse_lazy("manage")
    fields = ["slug", "destination_url"]


class DestinationDeleteView(NoGetMixin, DeleteView):
    model = Destination
    success_url = reverse_lazy("manage")


def redirect_view(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    destination.add_visit()
    return HttpResponsePermanentRedirect(destination.destination_url)
