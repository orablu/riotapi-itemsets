"""Data models for the riot api."""

from riot_api import STATIC_API

class MatchData(object):
    """Match data."""

    matches = 0

    def __init__(self, match_id, won, champion, items, wards, vision_wards):
        MatchData.matches += 1
        self.match_id = match_id
        self.won = won
        self.champion = champion
        self.items = items
        self.wards = wards
        self.vision_wards = vision_wards

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
        return matches / MatchData.matches, self.wins / matches, self.losses / matches

    def __hash__(self):
        return self.item_id
