#!encoding: utf-8
from django.shortcuts import render
from achievement_display.models import Baidumetasource
import time
import linkedin

# Create your views here.

def index(request):
    uri = 'http://192.168.120.17:9206/datahouse/records/_search?pretty'

    context = {}

    #获取文库总的采集总数
    context['wenku_all_collection'] = Baidumetasource.objects.all().count()
    #获取文库昨天采集总数
    yesterday = time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))
    context['wenku_yesterday_collection'] = Baidumetasource.objects.filter(crawltime=yesterday).count()

    #获取主页采集总数
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    context['homepage_all_collection'] = linkedin.get_total(uri)
    context['homepage_yesterday_collection'] = linkedin.search(uri, yesterday, today)



    return render(request, 'achievement_display/index.html', context)
