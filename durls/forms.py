from django.forms import ModelForm

from durls.models import Destination


class DestinationForm(ModelForm):
    
    class Meta:
        model = Destination
        fields = ("slud", "destination_url")
