from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponse

from models import Summoner

def index(request):
    summoner_list = Summoner.objects.order_by('summoner_name')[:5]
    context = RequestContext(request, { 'summoner_list': summoner_list })
    return render(request, 'itemviewer/index.html', context)

def summoner(request, summoner_id):
	summoner = get_object_or_404(Summoner, summoner_id=summoner_id)
	context = RequestContext(request, { 'summoner': summoner })
	return render(request, 'itemviewer/summoner.html', context)

def match(request, match_id):
	match = get_object_or_404(Match, match_id=match_id)
	context = RequestContext(request, { 'match': match })
	return render(request, 'itemviewer/match.html', context)
