#!encoding: utf-8
from django.shortcuts import render
from achievement_display.models import *
import time
import linkedin
import tor
import json


"""
该函数返回N天以前得日期,例如n = 1就是返回一天
以前得日期,也就是昨天
"""
def return_n_day(n=0):
    return time.strftime('%Y-%m-%d',time.localtime(time.time()-86400*n))

# Create your views here.

def index(request):
    uri = 'http://192.168.120.17:9206/datahouse/records/_search?pretty'
    uri2 = 'http://192.168.120.17:9206/hiddenwebs/hiddenwebpages/_search?pretty'

    #define time
    today = return_n_day(0)
    today_1 = return_n_day(1)
    today_2 = return_n_day(2)
    today_3 = return_n_day(3)
    today_4 = return_n_day(4)

    context = {}

    #获取文库总的采集总数
    context['wenku_all_collection'] = Baidumetasource.objects.all().count()
    context['wenku_yesterday_collection'] = Baidumetasource.objects.filter(crawltime=today_1).count()
    today_1_data = Baidumetasource.objects.filter(crawltime__lte=today_1).count()
    today_2_data = Baidumetasource.objects.filter(crawltime__lte=today_2).count()
    today_3_data = Baidumetasource.objects.filter(crawltime__lte=today_3).count()

    #获取文库昨天采集总数
    yesterday = return_n_day(1)
    #文库图表
    context['wenku_x'] = json.dumps([today_3[-5:], today_2[-5:], today_1[-5:], today[-5:]])
    context['wenku_y'] = json.dumps([today_3_data, today_2_data, today_1_data, context['wenku_all_collection']])

    #获取学术总数
    context['scholar_all_collection'] = Wanfangmetasource.objects.all().using('ScholarInfoBase').count()
    context['scholar_yesterday_collection'] = Wanfangmetasource.objects.using('ScholarInfoBase').filter(crawltime=today_1).count()
    today_1_data_schoolar = Wanfangmetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=today_1).count()
    today_2_data_schoolar = Wanfangmetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=today_2).count()
    today_3_data_schoolar = Wanfangmetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=today_3).count()
    context['scholar_x'] = json.dumps([today_3[-5:], today_2[-5:], today_1[-5:], today[-5:]])
    context['scholar_y'] = json.dumps([today_3_data_schoolar, today_2_data_schoolar, today_1_data_schoolar, context['scholar_all_collection']])

    #获取主页采集总数
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    context['homepage_all_collection'] = linkedin.get_total(uri)
    context['homepage_yesterday_collection'] = linkedin.search(uri, yesterday, today)

    #获取暗网采集总数
    #today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    context['anwang_all_collection'] = tor.get_total(uri2)
    #context['homepage_yesterday_collection'] = linkedin.search(uri, yesterday, today)

    return render(request, 'achievement_display/index.html', context)
