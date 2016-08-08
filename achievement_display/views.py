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
import sys




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

def sub_string(string, num):
    """
    截取字符串函数
    :param string: 传入字符串
    :param num: 截取数量
    :return:
    """
    sub_str = string.decode('utf8')[0:num].encode('utf8')
    if(len(string.decode('utf8'))>num):
        return sub_str+'...'
    else:
        return sub_str

def edit_distance(s1, s2):
    """
    编辑距离
    :param s1: 字符串1
    :param s2: 字符串2
    :return:
    """
    def get(ii, jj):
        if ii < 0 or jj < 0:
            return max(ii, jj) + 1
        return a[ii * n2 + jj]

    n1, n2 = len(s1), len(s2)
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    if s1 == s2:
        return 0
    a = [0] * (n1 * n2)
    i = 0
    while i < n1:
        j = 0
        while j < n2:
            if s1[i] == s2[j]:
                a[i * n2 + j] = get(i - 1, j - 1)
            else:
                a[i * n2 + j] = min(get(i - 1, j - 1), get(i - 1, j), get(i, j - 1)) + 1
            j += 1
        i += 1
    return a[n1 * n2 - 1]

def find_optimal_card(list, s_value):
    """
    通过编辑距离查找出最合适的匹配
    :param list: 传入的列表
    :param s_value: 查询的字符串
    :return: 返回含有一个值的列表
    """
    opt_list = []
    opt_list.append(list[0])
    opt_name = list[0]['_source']['name']
    opt_score = (edit_distance(opt_name, s_value), -len(list[0]['_source']))

    for x in list:
        score = (edit_distance(x['_source']['name'], s_value), -len(x['_source']))
        if score < opt_score:
            opt_list[0] = x
            opt_score = score

    return opt_list




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

    #获取百科采集总数
    context['baike_all_collection'] = BaiduBaike.objects.all().using('knowledge_base').count() + 1132716
    context['baike_yesterday_collection'] = BaiduBaike.objects.using('knowledge_base').filter(crawltime__lte=return_hour_day(1)).filter(crawltime__gte=return_hour_morning_day(1)).count() + 0

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
        context['baidubaike'] = dict['baidubaike']


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
        context['sort_en'] = request.GET['sort']
        s = Search()

        """
        判断是否有敏感性排序
        """
        if context['sort_en'] == "sensitiveness":
            context['sort'] = "敏感性"
        else:
            context['sort'] = "相关性"


        """
        查询时间和显示数量
        """
        res = s.s_search(context['paper_type'], context['form_option'], context['input_value'], 0, 1,  context['sort_en'])
        context['total'] = res['total']
        context['time'] = res['time']

        """
        查询出卡片的内容
        """
        type = ['Corporation', 'Person', 'ResearchOrganization', 'EducationalOrganization', 'weapon']
        # card_res = s.card_search(type, context['input_value'], 0 , 1)
        card_res_raw = s.card_search(type, context['input_value'], 0 , 5)
        if(card_res_raw['result_content']):
            card_res = find_optimal_card(card_res_raw['result_content'], context['input_value'])
        else:
            card_res = card_res_raw['result_content']

        context['card_res'] = json.dumps(card_res)
        """
        获取请求路径
        """
        # context['request_path'] = request.get_full_path()
        context['request_path'] = request.GET


        return render(request, 'achievement_display/search.html', context)
        # return HttpResponse(card_res)
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
            sort = request.GET['sort']
        else:
            curr = 1


    except:
        curr = 1
    pagesize = 10
    fromsize = (int(curr)-1) * pagesize
    s = Search()
    #res = s.search(keyvalue, fromsize, pagesize)
    res = s.s_search(paper_type, body_type, keyvalue, fromsize, pagesize, sort)
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

def ajax_agg(request):
    """
    ajax聚合查询
    :param request:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf8')
    s = Search()
    if "fields" in request.GET:
        keyvalue = request.GET['keyvalue']
        paper_type = request.GET['papertype']
        body_type = request.GET['bodytype']
        fields = request.GET['fields']
        res = s.list_agg_search(paper_type, body_type, keyvalue, fields)
        dict_res = res['aggregations']['all_journals']['buckets']
        string = ''
        if fields == 'sourceOrganization':
            for x in dict_res:
                string += '<li class="list-group-item condition-li"><span class="con-li-span">'+str(x['doc_count'])+'篇</span><a href="#" title="'+str(x['key'].split('|')[1])+'" class="con-li-a"><input name="filter-org" type="checkbox" value="'+str(x['key'])+'" >&nbsp;'+sub_string(str(x['key'].split('|')[1]), 7)+'</a></li>'
        else:
            for x in dict_res:
                string += '<li class="list-group-item condition-li"><span class="con-li-span">'+str(x['doc_count'])+'篇</span><a href="#" title="'+str(x['key'])+'" class="con-li-a"><input name="filter-subject" type="checkbox" value="'+str(x['key'])+'" >&nbsp;'+sub_string(str(x['key']), 7)+'</a></li>'

        return HttpResponse(string)


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
    # try:
    #     id = request.GET['id']
    #     type = request.GET['type']
    #     s = Search()
    #     res = s.search_in_id(id, type, 0, 1)
    #     return HttpResponse(json.dumps(res['res_content']))
    #
    # except:
    #     return HttpResponse("none")

    id = request.GET['id']
    type = request.GET['type']
    s = Search()
    res = s.search_in_id(id, type, 0, 1)
    return HttpResponse(json.dumps(res['result_content']))


def force_open(request):
    """
    知识图谱视图函数
    :param requesr:
    :return:
    """
    g = Search()
    context = {}      #初始化字典
    MAX_DISPLAY_NUM = 9     #主页显示的实体最大数量
    _id = "ResearchOrganization/1000011424|中国科学院信息工程研究所"  #_id = "EducationalOrganization/1000010463|湖南科技大学中文系"
    context['id'] = request.GET['id']

    """
    查询出该组织的head
    """
    res_head = g.find_one_by_id(context['id'].split("|")[0].split("/")[0], context['id'].split("/")[1].split("|")[0])
    if res_head:
        # try:
        #     if res_head['result_content']['_source'].has_key("head"):
        #         context['head_workfor'] = res_head['result_content']['_source']['head']
        #         context['head_workfor_relationship'] = "领导"
        #     if res_head['result_content']['_source'].has_key("worksFor"):
        #         context['head_workfor'] = res_head['result_content']['_source']['worksFor']
        #         context['head_workfor_relationship'] = "工作单位"
        # except:
        #     pass
        if res_head['result_content'][0]['_source'].has_key("head"):
            context['head_workfor'] = json.dumps(res_head['result_content'][0]['_source']['head'])
            context['head_workfor_relationship'] = "负责人"
        if res_head['result_content'][0]['_source'].has_key("worksFor"):
            list_workfor = []
            list_workfor.append(res_head['result_content'][0]['_source']['worksFor'])
            context['head_workfor'] = json.dumps(list_workfor)
            context['head_workfor_relationship'] = "工作单位"

    """
    先从数据中取出9个
    """
    res = g.graph_search(context['id'], 0, MAX_DISPLAY_NUM)
    context['total'] = res['total']
    context['name'] = context['id'].split("|")[1]
    """
    判断数据库中的数据是否大于9个,如果大于则返回剩余数据
    """
    if(context['total'] > MAX_DISPLAY_NUM):
        res_left = g.graph_search(context['id'], MAX_DISPLAY_NUM, context['total'])
        context['res_content_left'] = json.dumps(res_left['result_content'])
    else:
        context['res_content_left'] = 0   #判断是否有数据

    context['res_content'] = json.dumps(res['result_content'])
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

