from django.contrib import admin

from cities.models import Route, City, AnchorPoint
from .city_form import CityAdminForm

class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ('id', 'name', 'visible')
    list_display_links = ('id', 'name')
    list

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "routes":
            kwargs["queryset"] = Route.objects.filter(active=True)
    
        elif db_field.name == "points":
            kwargs["queryset"] = AnchorPoint.objects.filter(active=True)
            
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    

admin.site.register(City, CityAdmin)