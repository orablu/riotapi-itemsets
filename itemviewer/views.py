from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from models import Summoner

def index(request):
    summoner_list = Summoner.objects.order_by('name')[:5]
    context = RequestContext(request, {
        'summoner_list': summoner_list,
    })
    return render(request, 'itemviewer/index.html', context)

def summoner(request, summoner_id):
	try:
		summoner = Summoner.objects.get(pk=summoner_id)
	except Summoner.DoesNotExist:
	    return Http404('Summoner {summoner_id} does not exist.'.format(
	    	summoner_id=summoner_id
    	))

def match(request, match_id):
	try:
		match = Match.objects.get(pk=match_id)
	except Match.DoesNotExist:
	    return Http404('Match {match_id} does not exist.'.format(
	    	match_id=match_id
    	))
