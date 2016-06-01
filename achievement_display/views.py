#!encoding: utf-8
from django.shortcuts import render
from achievement_display.models import *
from django.http import HttpResponse, HttpResponseRedirect
from achievement_display.pyclass.GetHighChartData import GetHighChartData
from achievement_display.pyclass.Search import Search
from achievement_display.pyclass.DataTable import OrderListJson
import time
import linkedin
import tor
import json
from open_source import  test2



"""
功能性函数
该函数返回N天以前得日期,例如n = 1就是返回一天
以前得日期,也就是昨天
"""
def return_n_day(n=0):
    return time.strftime('%Y-%m-%d',time.localtime(time.time()-86400*n))

def return_hour_day(n=0):
    return time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time()-86400*n))
    #return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-86400*n))
    #return str(int(time.time()-86400*n))

def return_hour_morning_day(n=0):
    return time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()-86400*n))
# Create your views here.


"""
视图型函数
"""
def judge_type(date_type):
    if "worksFor" in date_type:
        return "person"
    else:
        return "organization"


def index(request):
    uri = 'http://192.168.120.17:9206/datahouse/records/_search?pretty'
    uri2 = 'http://192.168.120.17:9206/hiddenwebs_v2/hiddenwebpages/_search?pretty'

    #define time
    today = return_n_day(0)
    today_1 = return_n_day(1)
    today_2 = return_n_day(2)
    today_3 = return_n_day(3)
    today_4 = return_n_day(4)

    context = {}

    #获取文库总的采集总数
    context['wenku_all_collection'] = Baidumetasource.objects.all().count()
    context['wenku_yesterday_collection'] = Baidumetasource.objects.filter(crawltime__lte=return_hour_day(1)).filter(crawltime__gte=return_hour_morning_day(1)).count()
    context['secret_check_alert'] = Docbmcheckresult.objects.exclude(alertnum=0).all().count()
    context['secret_check'] = Docbmcheckresult.objects.all().count()
    context['yx_check_alert'] = Picyxcheckresult.objects.all().count()
    context['yx_check'] = Docyxcheckresult.objects.all().count()

    #获取文库昨天采集总数
    yesterday = return_n_day(1)


    #获取学术总数
    context['scholar_all_collection'] = Wanfangmetasource.objects.all().using('ScholarInfoBase').count() + Acmmetasource.objects.all().using('ScholarInfoBase').count() + Ieeemetasource.objects.all().using('ScholarInfoBase').count()+ Cnkimetasource.objects.all().using('ScholarInfoBase').count()
    wanfang_num = Wanfangmetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=return_hour_day(1)).filter(crawltime__gte=return_hour_morning_day(1)).count()
    acm_num = Acmmetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=return_hour_day(1)).filter(crawltime__gte=return_hour_morning_day(1)).count()
    ieee_num = Ieeemetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=return_hour_day(1)).filter(crawltime__gte=return_hour_morning_day(1)).count()
    cnki_num = Cnkimetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=return_hour_day(1)).filter(crawltime__gte=return_hour_morning_day(1)).count()
    context['scholar_yesterday_collection'] = wanfang_num + acm_num + ieee_num + cnki_num

    #获取主页采集总数
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    context['homepage_all_collection'] = linkedin.get_total(uri)
    context['homepage_yesterday_collection'] = linkedin.search(uri, yesterday, yesterday)

    #获取暗网采集总数
    context['anwang_all_collection'] = tor.get_total(uri2)
    context['anwang_yesterday_collection'] = tor.search(uri2, yesterday, yesterday)

    return render(request, 'achievement_display/index.html', context)


def highchart(request):
    get_data = GetHighChartData()
    name = request.GET.get('name')
    context = {}
    context['name'] = name

    """
    文库数据赋值
    """
    if name == 'wenku':
        dict = get_data.wenku(7, name)
        context['date_no_hour'] = dict['date_no_hour']
        context['wenku_caiji_data'] = dict['wenku_caiji_data']
        context['secret_check_alert'] = dict['secret_check_alert']
        context['secret_check'] = dict['secret_check']
        context['yx_check_alert'] = dict['yx_check_alert']
        context['yx_check'] = dict['yx_check']

    """
    万方数据采集
    """
    if name == 'schoolar':
        dict = get_data.schoolar(7, name)
        context['date_no_hour_schoolar'] = dict['date_no_hour']
        context['wanfang'] = dict['wanfang']
        context['acm'] = dict['acm']
        context['ieee'] = dict['ieee']
        context['cnki'] = dict['cnki']
        # context['cnki'] = [1 ,2, 3, 4, 5, 6, 7]

    """
    百科数据采集
    """
    if name == 'baike':
        dict = get_data.baike(7, name)
        context['date_no_hour_baike'] = dict['date_no_hour']
        context['baike'] = dict['baike']

    """
    linkedIn数据采集
    """
    if name == 'homepage':
        dict = get_data.homepage(7, name)
        context['date_no_hour_homepage'] = dict['date_no_hour']
        context['homepage'] = dict['linkedin']

    """
    anwang数据采集
    """
    if name == 'anwang':
        dict = get_data.anwang(7, name)
        context['date_no_hour_anwang'] = dict['date_no_hour']
        context['anwang'] = dict['anwang']

    return render(request, 'achievement_display/highchart.html', context)

def wenku(request):
    """
    保密检查的界面
    :param request:
    :return:
    """
    context = {}
    name = request.GET.get('name')

    context['secret_check_alert'] = Docbmcheckresult.objects.exclude(alertnum=0).all().count()
    context['secret_check'] = Docbmcheckresult.objects.all().count()
    context['yx_check_alert'] = Picyxcheckresult.objects.all().count()
    context['yx_check'] = Docyxcheckresult.objects.all().count()
    # context['secret_check_alert'] = Docbmcheckresult.objects.exclude(alertnum=0).all().count()
    # context['secret_check'] = Docbmcheckresult.objects.all().count()
    # context['yx_check_alert'] = Picyxcheckresult.objects.all().count()
    # context['yx_check'] = Docyxcheckresult.objects.all().count()
    if name == "1":
        context['res'] = Docbmcheckresult.objects.exclude(alertnum=0).all()
    elif name == "2":
        context['res'] = Picyxcheckresult.objects.all()
    elif name == "3":
        context['res'] = Docbmcheckresult.objects.all()
    elif name == "4":
        context['res'] = Docyxcheckresult.objects.all()

    context['name'] = name

    return render(request, 'achievement_display/wenku.html', context)

def datatables_iframe(request):
    """
    保密检查的界面
    :param request:
    :return:
    """
    context = {}

    return render(request, 'achievement_display/datatables_iframe.html', context)

def search(request):
    """
    搜索界面
    """
    from_size = 0
    page_size = 20
    if "keyvalue" in request.GET:
        context = {}
        context['input_value'] = request.GET['keyvalue']
        context['paper_type'] = request.GET['paper-type']
        context['form_option'] = request.GET['form-option']
        # context['content'] = source
        # context['total'] = res['total']
        # context['time'] = res['time']
        return render(request, 'achievement_display/search.html', context)
    else:
        return HttpResponseRedirect("index")

def search2(request):
    """
    搜索界面
    """
    from_size = 0
    page_size = 20
    if "keyvalue" in request.GET:
        s = Search()
        res = s.search(request.GET['keyvalue'], from_size,  page_size)
        context = {}
        source = []
        context['input_value'] = request.GET['keyvalue']
        for x in res['result_content']:
            dict = x['_source']
            dict['judge_type'] = judge_type(dict)
            source.append(dict)
        context['content'] = source
        context['total'] = res['total']
        context['time'] = res['time']
        return render(request, 'achievement_display/search_test.html', context)
    else:
        return HttpResponseRedirect("index")


def ajax_page(request):
    """
    ajax分页
    大坑!!!get接受的是字符串类型,在进行加减乘除的时候一定要进行整型转换
    :param request:
    :return:
    """
    try:
        if "page" in request.GET:
            curr = request.GET['page']
            keyvalue = request.GET['keyvalue']
            paper_type = request.GET['papertype']
            body_type = request.GET['bodytype']
        else:
            curr = 1
    except:
        curr = 1
    pagesize = 10
    fromsize = (int(curr)-1) * pagesize
    s = test2.Search()
    #res = s.search(keyvalue, fromsize, pagesize)
    res = s.s_search(paper_type, body_type, keyvalue, fromsize, pagesize)
    res['total'] = int(res['total']) / pagesize
    """
    测试参数
    """
    # try:
    #     if "page" in request.GET:
    #         curr = request.GET['page']
    #         keyvalue = request.GET['keyvalue']
    #     else:
    #         curr = 1
    #         keyvalue = "null"
    # except:
    #     curr = 1
    #     keyvalue = "1"
    #
    # res = {}
    # res['par'] = keyvalue


    return HttpResponse(json.dumps(res))

def force(request):
    """
    知识图谱视图函数
    :param requesr:
    :return:
    """
    context = {}
    return render(request, "achievement_display/force.html", context)

def get_node_info(request):
    """
    通过AJAX请求获取节点信息
    :param get_node_info:
    :return:
    """
    if "id" in request.GET:
        s = Search()
        res = s.search_in_id(request.GET['id'])
        context = {}
        context['name'] = res['result_content']['_source']['name']
        context['id'] = res['result_content']['_id']
        context['desc'] = res['result_content']['_source']['description']
        return HttpResponse(json.dumps(context))
    else:
        return HttpResponse("none")

def force_open(request):
    """
    知识图谱视图函数
    :param requesr:
    :return:
    """
    context = {}
    return render(request, "achievement_display/force_open.html", context)


def test(request):
    #return HttpResponse(Docbmcheckresult.objects.all().count())
    context = {}
    return render(request, "achievement_display/wenku.html", context)

def convert_id_name(request):
    """
    将表格中的ID转换为名称
    :param request:
    :return:
    """
    try:
        string = request.GET['id']
        #string = "BDWK_0000798204a1b0717ed5dd6c"
        res = Baidumetasource.objects.get(id=string)
        if res:
            return HttpResponse(res.filename)
        else:
            return HttpResponse("无")
    except:
        return HttpResponse("无名称")

