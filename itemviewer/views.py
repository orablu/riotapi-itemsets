from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('At item viewer index!')

def summoner(request, summoner_id):
    return HttpResponse('At item viewer summoner profile!')

def match(request, match_id):
    return HttpResponse('At item viewer match profile!')