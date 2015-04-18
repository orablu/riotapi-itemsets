"""Riot Games API request constants."""

API_VERSIONS = {
    'static': '5.2.1',
    'summoner': '1.4',
    'matchhistory': '2.2',
}

REGIONS = {
    'global': 'global',
    'north_america': 'na',
}

LANGUAGES = {
    'english': 'en_US',
}

URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'match_history_by_id': 'v{version}/matchhistory/{summonerId}',

    'static_base': 'http://ddragon.leagueoflegends.com/cdn/{version}/{url}',
    'item_icon': 'img/item/{itemId}',
    'item_data': 'data/{language}/item.json',
    'champion_icon': 'img/champion/{championName}',
}

