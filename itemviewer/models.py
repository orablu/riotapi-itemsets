"""Item Viewer models."""

from django.db import models

class Summoner(models.Model):
    """A summoner database object."""
    summoner_name = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Summoner {0}'.format(self.summoner_name)

