from django.contrib import admin
from .models import MatchsAVenir, Iframe, Data


@admin.register(MatchsAVenir)
class MatchAVenir(admin.ModelAdmin):
    list_display = (
        "date", "match", "championship", "card_bet", "corner_bet", "real_cards", "real_corners", "card_bet_passed",
        "corner_bet_passed")
    list_filter = ("date", "championship", "card_bet")
    search_fields = ("championship", "home_team", "away_team")


@admin.register(Iframe)
class Iframe(admin.ModelAdmin):
    list_display = ("championship", "iframe_url", "iframe_stats", "date_updated")


@admin.register(Data)
class Data(admin.ModelAdmin):
    list_display = ('championship', 'datas', "datas_stats", "date_updated")
