"""Riot Games API item set generator."""

from riot_api import RiotApi
from riot_api import RiotApiHelper
import private_consts as ApiKey

def main():
    """
    Get the given summoner name (if any) and generate some item sets based off
    of their recent matches.
    """
    api = RiotApi(ApiKey.API_KEY)
    helper = RiotApiHelper(api)
    json = helper.get_match_history_by_name('ora')
    print json

if __name__ == '__main__':
    main()

