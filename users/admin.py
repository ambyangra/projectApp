from django.contrib import admin
from .src.models import *

admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(LeagueAdmin)
admin.site.register(Game)
admin.site.register(Tournament)