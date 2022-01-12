from django.views.generic import TemplateView, CreateView, DeleteView
from durls.models import Destination
from django.shortcuts import get_object_or_404
from django.http import HttpResponsePermanentRedirect, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "durls/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = Destination.objects.all()
        return context


class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    success_url = reverse_lazy("create")
    template_name = "durls/destination_list.html"
    fields = ["slug", "destination_url"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = self.model.objects.all()
        return context


class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    model = Destination
    success_url = reverse_lazy("create")
    template_name = "durls/destination_delete.html"

    def get_object(self, queryset=None):
        """Hook to ensure object is owned by request.user."""
        obj = super().get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


def redirect_view(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    destination.add_visit()
    return HttpResponsePermanentRedirect(destination.destination_url)
