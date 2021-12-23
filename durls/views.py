from django.views.generic import TemplateView, ListView
from durls.models import Destination
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):
    template_name = "durls/home.html"


class DestinationListView(ListView):
    model = Destination
    template_name = "destination_list.html"


def redirect_view(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    return HttpResponseRedirect(destination.destination_url)
