from riot_api import RIOT_API as API, STATIC_API
from itemviewer.models import *

def query_recent_matches(summoner):
    matches = API.get_match_history(summoner.summoner_id)
    for match in matches:
        if len(Match.objects.filter(match_id=match['matchId'])) > 0:
            continue
        m = Match(
            main_summoner=summoner,
            match_type=match['queueType'],
            match_id=match['matchId'],
            match_duration=match['matchDuration'])
        m.save()
        for participant in match['participants']:
            for participant_identity in match['participantIdentities']:
                if participant_identity['participantId'] == participant['participantId']:
                    identity = participant_identity['player']
            s = Summoner.objects.get_or_create(
                summoner_id=identity['summonerId'],
                summoner_name=identity['summonerName'])
            s.save()
            p = Participant(
                match=m,
                summoner=s,
                champion_id=participant['championId'],
                is_opponent=(participant['teamId'] != summoner['teamId']),
                match_won=participant['stats']['winner'],
                wards=participant['stats']['wardsPlaced'])
            p.save()
            # TODO: Add items