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

    main_summoner = models.ForeignKey(Summoner)
    match_type = models.CharField(max_length='50', default='Unknown')
    match_id = models.IntegerField(unique=True, default=0)
    match_duration = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Match {0}: {1}, {2}, {3} sight wards, {4} vision wards'.format(
            self.match_id,
            self.champion,
            self.items,
            self.wards,
            self.vision_wards
        )

class Participant(models.Model):
    """Represents the match data for a participant in the match."""

    match = models.ForeignKey(Match)
    summoner = models.ForeignKey(Summoner)
    champion_id = models.IntegerField(default=0)
    is_opponent = models.BooleanField(default=True)
    match_won = models.BooleanField(default=False)
    wards = models.IntegerField(default=0)

    def set_participant_from_data(self, participant, teams, main_team_id = None):
        self.champion_id = participant['championId']
        self.is_opponent = main_team_id and participant['teamId'] != main_team_id
        for team in teams:
            if team['teamId'] == participant['teamId']:
                self.match_won = team['winner']
        item_ids = [
            participant['stats']['item0'],
            participant['stats']['item1'],
            participant['stats']['item2'],
            participant['stats']['item3'],
            participant['stats']['item4'],
            participant['stats']['item5'],
            participant['stats']['item6'],
        ]
        self.wards = participant['stats']['wardsPlaced']
        for item_id in item_ids:
            if item_id is not 0:
                item = Item.objects.get_or_create(item_id=item_id)
                item.participants.add(self)

class Item(models.Model):
    """Represents an item and its usage stats."""

    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=50, default='')
    icon_url = models.CharField(max_length=300, default='')
    participants = models.ManyToManyField(Participant)

    def __init__(self, item_id):
        self.item_id = item_id
        self.item_name = STATIC_API.get_item_name(item_id)
        self.icon_url = STATIC_API.get_item_icon(item_id)

    def __hash__(self):
        return self.item_id

