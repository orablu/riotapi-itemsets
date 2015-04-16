"""Data models for the riot api."""

class MatchData(object):
    """Match data."""

    def __init__(self, match_id, champion, items, wards, vision_wards):
        self.match_id = match_id
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
