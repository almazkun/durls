from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from durls.models import Destination

# Create your views here.
class DestinationListView(ListView):
    model = Destination
    template_name = "destination_list.html"


class DestinationCreateView(CreateView):
    model = Destination

    def get_success_url(self):
        return reverse_lazy("destination_list")
