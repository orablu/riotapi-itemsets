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

    def get_summoner_id_by_name(self, name):
        """Gets the id associated with the given summoner name."""
        return self.get_summoner_by_name(name)[name]['id']

    def get_match_history_by_name(self, name):
        """Gets the match history associated with the given summoner name."""
        return self.get_match_history(self.get_summoner_id_by_name(name))

    def get_recent_stats_by_name(self, name):
        """Gets the recent stats associated with the given summoner name."""
        matches = self.get_match_history_by_name(name)
        matches = matches['matches']
        stats = []
        for match in matches:
            participant = match['participants'][0]
            p_champion = participant['championId']
            p_stats = participant['stats']
            p_stats['championId'] = p_champion
            stats.append(p_stats)
        return stats

    def get_recent_builds_by_name(self, name):
        """Gets the recent item builds associated with the given summoner name."""
        stats_per_match = self.get_recent_stats_by_name(name)
        f_stats_per_match = [
            {
                'championId': stats['championId'],
                'items': [
                    stats['item0'],
                    stats['item1'],
                    stats['item2'],
                    stats['item3'],
                    stats['item4'],
                    stats['item5'],
                    stats['item6'],
                ],
                'wards': stats['sightWardsBoughtInGame'],
                'visionWards': stats['visionWardsBoughtInGame'],
            }
            for stats in stats_per_match
        ]
        return f_stats_per_match

