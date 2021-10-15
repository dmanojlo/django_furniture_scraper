from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from scrapyd_api import ScrapydAPI
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json, urllib.request
# Create your views here.

scrapyd = ScrapydAPI('http://localhost:6800')
#scrapyd = ScrapydAPI('http://randmovie-scraper.herokuapp.com/')

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def home(request):
    data = dict()
    # settings = {
    #         'FEED_URI': 'result.json',
    #         'FEED_FORMAT': 'json'
    #     }
    task = ''
    if request.method == 'POST':
    # task_id = request.GET.get('task_id', None)
    # print(task_id)
    # if task_id is None:
        task = scrapyd.schedule('default', 'mima')
        return JsonResponse({'task':task})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            task_id = task_id[:-1]
            #print(task_id)
        status = scrapyd.job_status('default', task_id)
        #print(status)
        if status == 'finished':
            with open(r"C:\Users\dmanojlovic\Documents\furniture_scraper\furniture_scraper\mima_result.json") as f:
            #with urllib.request.urlopen("https://randmovie-scraper.herokuapp.com/logs/result.json") as f:
                jso = json.load(f)
            print('ovo je id')
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'furniture/home.html', {})

# def home(request):
#     return render(request, 'furniture/home.html', {})


# Create your views here.
