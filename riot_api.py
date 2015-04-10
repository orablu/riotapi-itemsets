"""Riot Games API requests."""

import consts as Consts
import requests
import requests.packages.urllib3.contrib.pyopenssl as pyopenssl

pyopenssl.inject_into_urllib3()

class RiotAPI(object):
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

    def get_summoner_by_name(self, name):
        """Gets the summoner data belonging to the summoner name."""
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name)
        return self._request(api_url)

    def get_match_history(self, summoner):
        """Gets the match history of the given summoner."""
        api_url = Consts.URL['match_history_by_id'].format(
            version=Consts.API_VERSIONS['matchhistory'],
            summonerId=summoner)
        return self._request(api_url)

