"""Riot Games API request constants."""

URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'match_history_by_id': 'v{version}/matchhistory/{summonerId}',
}

API_VERSIONS = {
    'summoner': '1.4',
    'matchhistory': '2.2',
}

REGIONS = {
    'global': 'global',
    'north_america': 'na',
}

