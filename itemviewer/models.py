"""Item Viewer models."""

from django.db import models
from viewmodels.riot_api import STATIC_API

class Summoner(models.Model):
    """A summoner database object."""

    summoner_name = models.CharField(unique=True, max_length=50, default='')
    summoner_id = models.IntegerField(unique=True, default=0)

    def __unicode__(self):
        return 'Summoner {0}'.format(self.summoner_name)

class Match(models.Model):
    """Match data."""

    summoner = models.ForeignKey(Summoner)
    match_id = models.IntegerField(unique=True, default=0)
    match_won = models.BooleanField(default=False)
    champion = models.IntegerField(default=0)
    item0 = models.IntegerField(null=True)
    item1 = models.IntegerField(null=True)
    item2 = models.IntegerField(null=True)
    item3 = models.IntegerField(null=True)
    item4 = models.IntegerField(null=True)
    item5 = models.IntegerField(null=True)
    item6 = models.IntegerField(null=True)
    wards = models.IntegerField(default=0)
    vision_wards = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Match {0}: {1}, {2}, {3} sight wards, {4} vision wards'.format(
            self.match_id,
            self.champion,
            self.items,
            self.wards,
            self.vision_wards
        )

class Item(object):
    """Represents an item and its usage stats."""

    def __init__(self, item_id):
        self.item_id = item_id
        self.name = STATIC_API.get_item_name(item_id)
        self.icon_url = STATIC_API.get_item_icon(item_id)
        self.matches = []
        self.wins = 0
        self.losses = 0

    def add_match(self, match_id, won):
        """Adds a match to the stats (unless it already exists)."""
        if match_id in self.matches:
            return
        self.matches.append(match_id)
        if won:
            self.wins += 1
        else:
            self.losses += 1

    def get_stats(self):
        """Get item frequency, win percent, and loss percent."""
        matches = self.wins + self.losses
        return matches / Match.objects.count, self.wins / matches, self.losses / matches

    def __hash__(self):
        return self.item_id
