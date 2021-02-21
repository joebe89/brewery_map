from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import BrewPoint

brew_mapping = {
    'name' : 'name',
    'street' : 'addr:street',
    'postcode' : 'addr:postcode',
    'city' : 'addr:city',
    'website' : 'website',
    'point' : 'POINT'
}

brew_gpkg = Path(__file__).resolve().parent / 'data' /'brew_eng.gpkg'

def run(verbose=True):
    lm = LayerMapping(BrewPoint, str(brew_gpkg), brew_mapping, layer='brew_eng', transform=False)
    lm.save(strict=True, verbose=verbose)
