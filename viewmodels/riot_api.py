"""Riot Games API requests."""

from private_consts import API_KEY
import consts as Consts
import requests
import requests.packages.urllib3.contrib.pyopenssl as pyopenssl

pyopenssl.inject_into_urllib3()

def _api_request(base_url, api_url, image=False, **kwargs):
    """Sends a request to the server, and returns the response in JSON form."""
    url = base_url.format(url=api_url)
    if image:
        return url
    else:
        return requests.get(url, params=kwargs).json()

class _StaticAPI(object):
    """Static API calls for the Riot Games API."""

    def __init__(self):
        self.base_url = Consts.URL['static_base'].format(
            version=Consts.API_VERSIONS['static'],
            url='{url}')

    def get_item_name(self, item_id):
        """Gets the name associated with the given item id."""
        api_url = Consts.URL['item_name'].format(language=Consts.LANGUAGES['english'])
        return _api_request(self.base_url, api_url)['data']['{id}'.format(id=item_id)]['name']

    def get_item_icon(self, item_id):
        """Gets the image associated with the item id."""
        api_url = Consts.URL['item_icon'].format(itemId=item_id)
        return _api_request(self.base_url, api_url, image=True)

    def get_champion_splash(self, champion_name):
        """Gets the splash image associated with the champion name."""
        api_url = Consts.URL['champion_splash'].format(championName=champion_name)
        return _api_request(self.base_url, api_url, image=True)

STATIC_API = _StaticAPI()

class _RiotAPI(object):
    """API calls for the Riot Games API."""

    def __init__(self, api_key, region=Consts.REGIONS['north_america']):
        """Creates new api wrapper for the given region (defaults to NA)."""
        self.api_key = api_key
        self.base_url = Consts.URL['base'].format(proxy=region, region=region, url='{url}')

    def _request(self, api_url, **kwargs):
        """Sends a request to the server, and returns the response in JSON form."""
        kwargs['api_key'] = self.api_key
        return _api_request(self.base_url, api_url, **kwargs)

    def get_summoner(self, *names):
        """Gets the summoner data belonging to the summoner name."""
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=','.join(names[:40]))
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
        count = max(1, min(count, 15))
        return self._request(api_url, beginIndex=min_id, endIndex=min_id+count)['matches']

RIOT_API = _RiotAPI(API_KEY)
