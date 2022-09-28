from django.db import models
from django.urls import reverse


class MatchsAVenir(models.Model):
    match = models.CharField(max_length=200)
    championship = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_team_cards_for_average = models.FloatField()
    away_team_cards_for_average = models.FloatField()
    home_team_cards_against_average = models.FloatField()
    away_team_cards_against_average = models.FloatField()
    home_team_corners_for_average = models.FloatField()
    away_team_corners_for_average = models.FloatField()
    home_team_corners_against_average = models.FloatField()
    away_team_corners_against_average = models.FloatField()
    card_bet = models.CharField(max_length=10)
    corner_bet = models.CharField(max_length=10)
    real_corners = models.IntegerField(blank=True, null=True)
    real_cards = models.IntegerField(blank=True, null=True)
    card_bet_passed = models.BooleanField(null=True)
    corner_bet_passed = models.BooleanField(null=True)

    def __str__(self):
        return self.match.replace("|", " - ")

    def get_absolute_url(self):
        return reverse("blog-match_detail", kwargs={"slug": self.slug})


class Iframe(models.Model):
    championship = models.CharField(max_length=200)
    iframe_url = models.URLField()
    iframe_stats = models.CharField(max_length=200)
    date_updated = models.CharField(max_length=200)


class Data(models.Model):
    championship = models.CharField(max_length=200)
    datas = models.JSONField()
    datas_stats = models.CharField(max_length=200)
    date_updated = models.CharField(max_length=200)
