from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView, RedirectView

from durls.models import Destination
from durls.forms import DestinationForm

# Create your views here.
class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationForm
    template_name = "destination_list.html"
    success_url = reverse_lazy("destination_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = Destination.objects.all()
        return context


def redirector(request, slug):
    if slug == "":
        redirect("https://akun.dev")
    destination = get_object_or_404(Destination, slug=slug)
    destination.add_visit()
    return redirect(destination.destination_url)


