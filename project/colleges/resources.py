from import_export import resources
from .models import CollegeDetails

class CollegeDetailsResource(resources.ModelResource):
    class Meta:
        model = CollegeDetails
class MapResource(resources.ModelResource):
    class Meta:
        model = Map
