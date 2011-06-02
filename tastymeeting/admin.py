from django.contrib import admin
from tastymeeting.models import *

# Admin display preferances

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'adresse', 'tel')
    
class MenuInline(admin.TabularInline):
    model = Menu
    extra = 3

class RepasAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'prix', 'places', 'date')
    inlines = [MenuInline]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'repas', 'date', 'transaction')
    
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('slug', 'description')


# Admin site registrations

admin.site.register(Ville)

admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(Repas, RepasAdmin)

admin.site.register(Reservation, ReservationAdmin)

admin.site.register(Badge, BadgeAdmin)