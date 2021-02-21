import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import BrewPoint

class BrewMapView(TemplateView):

    template_name = "map.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["brew"] = json.loads(serialize("geojson", BrewPoint.objects.all()))
        return context