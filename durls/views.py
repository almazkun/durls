from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from durls.models import Destination
from django.shortcuts import get_object_or_404
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "durls/home.html"


class DestinationCreateView(CreateView):
    model = Destination
    success_url = reverse_lazy("create")
    template_name = "durls/destination_list.html"
    fields = ["slug", "destination_url"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = self.model.objects.all()
        return context


class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = reverse_lazy("create")
    template_name = "durls/destination_delete.html"


def redirect_view(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    destination.add_visit()
    return HttpResponsePermanentRedirect(destination.destination_url)
