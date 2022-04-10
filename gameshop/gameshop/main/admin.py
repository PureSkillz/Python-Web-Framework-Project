from django.contrib import admin

from gameshop.main.models import Game, Periphery


@admin.register(Periphery)
class PeripheryAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
