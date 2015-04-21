from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from models import Summoner

def index(request):
    summoner_list = Summoner.objects.order_by('name')[:5]
    template = loader.get_template('itemviewer/index.html')
    context = RequestContext(request, {
        'summoner_list': summoner_list,
    })
    return HttpResponse(template.render(context))

def summoner(request, summoner_id):
    return HttpResponse('At item viewer summoner profile!')

def match(request, match_id):
    return HttpResponse('At item viewer match profile!')