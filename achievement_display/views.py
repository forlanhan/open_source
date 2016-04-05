#!encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from achievement_display.models import *
import time

# Create your views here.

def index(request):

    context = {}

    #获取文库总的采集总数
    context['all_collection'] = Baidumetasource.objects.all().count()

    #获取文库昨天采集总数
    yesterday = time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))
    context['yesterday_collection'] = Baidumetasource.objects.filter(crawltime=yesterday).count()

    return render(request, 'achievement_display/index.html', context)
