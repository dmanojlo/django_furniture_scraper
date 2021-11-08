from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from scrapyd_api import ScrapydAPI
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json, urllib.request
# Create your views here.

#scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd = ScrapydAPI('http://furniture-scrapyd.herokuapp.com/')

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def mima(request):
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
            #with open(r"C:\Users\dmanojlovic\Documents\furniture_scraper\furniture_scraper\mima_result.json", encoding='utf-8') as f:
            with urllib.request.urlopen("https://furniture-scrapyd.herokuapp.com/logs/mima_result.json", encoding='utf-8') as f:
                jso = json.load(f)
            #print('ovo je id')
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'furniture/mima.html', {})

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def emezzeta(request):
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
        task = scrapyd.schedule('default', 'emezzeta')
        return JsonResponse({'task':task})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            task_id = task_id[:-1]
            #print(task_id)
        status = scrapyd.job_status('default', task_id)
        #print(status)
        if status == 'finished':
            #with open(r"C:\Users\dmanojlovic\Documents\furniture_scraper\furniture_scraper\emezz_result.json", encoding='utf-8') as f:
            with urllib.request.urlopen("https://furniture-scrapyd.herokuapp.com/logs/emezz_result.json", encoding='utf-8') as f:
                jso = json.load(f)
            #print('ovo je id')
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'furniture/emezzeta.html', {})


@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def lesnina(request):
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
        task = scrapyd.schedule('default', 'lesnina')
        return JsonResponse({'task':task})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            task_id = task_id[:-1]
            #print(task_id)
        status = scrapyd.job_status('default', task_id)
        #print(status)
        if status == 'finished':
            #with open(r"C:\Users\dmanojlovic\Documents\furniture_scraper\furniture_scraper\lesnina_result.json", encoding='utf-8') as f:
            with urllib.request.urlopen("https://furniture-scrapyd.herokuapp.com/logs/lesnina_result.json", encoding='utf-8') as f:
                jso = json.load(f)
            #print('ovo je id')
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'furniture/lesnina.html', {})

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def prima(request):
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
        task = scrapyd.schedule('default', 'prima')
        return JsonResponse({'task':task})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            task_id = task_id[:-1]
            #print(task_id)
        status = scrapyd.job_status('default', task_id)
        #print(status)
        if status == 'finished':
            #with open(r"C:\Users\dmanojlovic\Documents\furniture_scraper\furniture_scraper\prima_result.json", encoding='utf-8') as f:
            with urllib.request.urlopen("https://furniture-scrapyd.herokuapp.com/logs/prima_result.json", encoding='utf-8') as f:
                jso = json.load(f)
            #print('ovo je id')
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'furniture/prima.html', {})

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def harvey(request):
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
        task = scrapyd.schedule('default', 'harvey')
        return JsonResponse({'task':task})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            task_id = task_id[:-1]
            #print(task_id)
        status = scrapyd.job_status('default', task_id)
        #print(status)
        if status == 'finished':
            #with open(r"C:\Users\dmanojlovic\Documents\furniture_scraper\furniture_scraper\harvey_result.json", encoding='utf-8') as f:
            with urllib.request.urlopen("https://furniture-scrapyd.herokuapp.com/logs/harvey_result.json", encoding='utf-8') as f:
                jso = json.load(f)
            #print('ovo je id')
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'furniture/harvey.html', {})

def home(request):
    return render(request, 'furniture/home.html', {})


# Create your views here.
