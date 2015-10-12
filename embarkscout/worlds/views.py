from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import WorldGenParams, World
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def getWorldToCreate(request):
    #wgp = WorldGenParams.objects.order_by('num_worlds')[0]
    wgp = WorldGenParams.objects.annotate(numworlds=Count('world')).order_by('numworlds')[0]
    world = World(world_gen_params=wgp)
    world.save()
    resp = {
        "world_id": world.id,
        "wgp_name": wgp.name,
        "wgp_seed": "RANDOM",
        "wgp_params": wgp.params.replace('\r', '')
    }
    return JsonResponse(resp)

@csrf_exempt
def submitWorld(request):
    print(str(request.body.decode('utf-8')))
    data = json.loads(str(request.body.decode('utf-8')))
    print(data)
    w = get_object_or_404(World, pk=data['id'])
    w.name = data['name']
    w.name_english = data['name_english']
    w.width = data['width']
    w.height = data['height']
    w.year = data['year']
    w.df_version = data['df_version']
    w.es_version = data['es_version']
    w.seed = data['seed']
    w.history_seed = data['history_seed']
    w.name_seed = data['name_seed']
    w.creature_seed = data['creature_seed']
    w.save()
    return JsonResponse({"success": True})

def index(request):
    return HttpResponse()