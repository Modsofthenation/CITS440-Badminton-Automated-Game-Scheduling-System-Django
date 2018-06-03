from django.contrib import admin
from personal.models import Team, Court, Game, Player, Booking, Availability


admin.site.register(Team)
admin.site.register(Court)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Booking)
admin.site.register(Availability)