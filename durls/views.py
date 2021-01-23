from django.views.generic import ListView, CreateView

from durls.models import Destination

# Create your views here.
class DestinationListView(ListView):
    model = Destination
    template_name = "destination_list.html"
