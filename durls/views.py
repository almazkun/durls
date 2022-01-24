from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView

from durls.models import Destination
from durls.services import destination_all, destination_for_user


class HomeView(TemplateView):
    template_name = "durls/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = destination_all()
        return context


class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    success_url = reverse_lazy("create")
    template_name = "durls/destination_list.html"
    fields = ["slug", "destination_url"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = destination_for_user(self.request.user)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        return super().form_valid(form)


class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    model = Destination
    success_url = reverse_lazy("create")
    template_name = "durls/destination_delete.html"

    def get_object(self, queryset=None):
        """Hook to ensure object is owned by request.user."""
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.is_staff:
            return obj
        raise Http404


def redirect_view(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    destination.add_visit()
    return HttpResponsePermanentRedirect(destination.destination_url)
