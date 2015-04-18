"""Riot Games API requests."""

from private_consts import API_KEY
import consts as Consts
from models import MatchData
import requests
import requests.packages.urllib3.contrib.pyopenssl as pyopenssl

pyopenssl.inject_into_urllib3()

class _StaticAPI(object):
    """Static API calls for the Riot Games API."""

    def __init__(self, api_key):
        """Creates new api wrapper for the given region (defaults to NA)."""
        self.api_key = api_key

    def _request(self, api_url, image=False, **kwargs):
        """Sends a request to the server, and returns the response in JSON form."""
        args = {'api_key': self.api_key}
        for key, value in kwargs.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['static_base'].format(
                version=Consts.API_VERSIONS['static'],
                url=api_url),
            params=args)
        if image:
            return response.content
        else:
            return response.json()

    def get_item_name(self, item_id):
        """Gets the name associated with the given item id."""
        api_url = Consts.URL['item_name'].format(language=Consts.LANGUAGES['english'])
        return self._request(api_url)['data']['{id}'.format(id=item_id)]['name']

    def get_item_icon(self, item_id):
        """Gets the image associated with the item id."""
        api_url = Consts.URL['item_icon'].format(itemId=item_id)
        return self._request(api_url, image=True)

    def get_champion_icon(self, champion_name):
        """Gets the image associated with the champion name."""
        api_url = Consts.URL['champion_icon'].format(championName=champion_name)
        return self._request(api_url, image=True)

STATIC_API = _StaticAPI(API_KEY)

class _RiotAPI(object):
    """API calls for the Riot Games API."""

    def __init__(self, api_key, region=Consts.REGIONS['north_america']):
        """Creates new api wrapper for the given region (defaults to NA)."""
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, **kwargs):
        """Sends a request to the server, and returns the response in JSON form."""
        args = {'api_key': self.api_key}
        for key, value in kwargs.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url),
            params=args)
        return response.json()

    def get_summoner(self, name):
        """Gets the summoner data belonging to the summoner name."""
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name)
        return self._request(api_url)

    def get_summoner_id(self, name):
        """Gets the id associated with the given summoner name."""
        return self.get_summoner(name)[name]['id']

    def get_match_history(self, summoner_id, min_id=0, count=15):
        """Gets the match history of the given summoner."""
        api_url = Consts.URL['match_history_by_id'].format(
            version=Consts.API_VERSIONS['matchhistory'],
            summonerId=summoner_id)
        min_id = min(min_id, 0)
        count = min(1, max(count, 15))
        return self._request(api_url, beginIndex=min_id, endIndex=min_id+count)

    def get_recent_stats(self, summoner_id):
        """Gets the recent stats associated with the given summoner name."""
        matches = self.get_match_history(summoner_id)
        matches = matches['matches']
        stats = []
        for match in matches:
            participant = match['participants'][0]
            p_champion = participant['championId']
            p_stats = participant['stats']
            p_stats['championId'] = p_champion
            stats.append(p_stats)
        return stats

    def get_recent_builds(self, summoner_id):
        """Gets the recent item builds associated with the given summoner name."""
        stats_per_match = self.get_recent_stats(summoner_id)
        return [
            MatchData(
                match_id=stats['matchId'],
                champion=stats['championId'],
                items=[
                    stats['item0'],
                    stats['item1'],
                    stats['item2'],
                    stats['item3'],
                    stats['item4'],
                    stats['item5'],
                    stats['item6'],
                ],
                wards=stats['sightWardsBoughtInGame'],
                vision_wards=stats['visionWardsBoughtInGame']
            )
            for stats in stats_per_match
        ]

RIOT_API = _RiotAPI(API_KEY)

