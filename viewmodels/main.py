"""Riot Games API item set generator."""

from riot_api import RiotAPI
import private_consts as ApiKey

def main():
    """
    Get the given summoner name (if any) and generate some item sets based off
    of their recent matches.
    """
    api = RiotAPI(ApiKey.API_KEY)
    json = api.get_recent_builds_by_name('ora')
    print json

if __name__ == '__main__':
    main()

