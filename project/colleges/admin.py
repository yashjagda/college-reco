from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import CollegeDetails,Caste,Location,Field,Map

#admin.site.register(CollegeDetails)
admin.site.register(Caste)
admin.site.register(Location)
admin.site.register(Field)
#admin.site.register(CollegeDetails)
@admin.register(CollegeDetails)
class CollegeDetailsAdmin(ImportExportModelAdmin):
    pass
@admin.register(Map)
class MapAdmin(ImportExportModelAdmin):
    pass
