from django.contrib import admin
from .models import PopularDestination, PopularPlace, RecentTrip, Question



class PopularDestinationAdmin(admin.ModelAdmin):
	list_display = ['title_place', 'date', 'slug',]
	list_filter = ['title_place', ]

admin.site.register(PopularDestination, PopularDestinationAdmin)

class PopularPlaceAdmin(admin.ModelAdmin):
	list_display = ['title_place', 'date', 'slug',]
	list_filter = ['title_place', ]





admin.site.register(PopularPlace, PopularPlaceAdmin)
admin.site.register(RecentTrip)
admin.site.register(Question)





# Register your models here.
