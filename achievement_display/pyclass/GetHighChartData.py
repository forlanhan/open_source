# encoding: utf-8
from achievement_display.models import *
import time
import json
from achievement_display import linkedin
from achievement_display import tor

"""
获取数据库中的数据
"""
class GetHighChartData:

    def g_get_no_hour_date(self, day):
        """
        该方法为一个生成器,获取离现在开始day之前的日期
        :param day:离现在开始day天
        :return:返回一个日期
        """
        while day > 0:
            yield time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400 * (day-1)))
            day = day - 1

    def g_get_hour_date(self, day):
        """
        该方法为一个生成器,获取离现在开始day之前的日期
        :param day:离现在开始day天
        :return:返回一个日期
        """
        while day > 0:
            yield time.strftime("%Y-%m-%d 23:59:59", time.localtime(time.time() - 86400 * (day-1)))
            day = day - 1

    def wenku(self, day, name):

        """
        获取文库相关的数据
        """

        date_no_hour = [x for x in self.g_get_no_hour_date(day)]
        date_hour = [x for x in self.g_get_hour_date(day)]
        dict = {}
        dict['date_no_hour'] = [x[-5:] for x in self.g_get_no_hour_date(day)]


        """
        文库数据采集
        """
        data_list = []
        for x in date_hour:
            num = Baidumetasource.objects.filter(crawltime__lte=x).all().count()
            data_list.append(num)
        dict['wenku_caiji_data'] = data_list

        """
        保密检查告警
        """
        data_list = []
        for x in date_hour:
            num = Docbmcheckresult.objects.filter(processtime__lte=x).exclude(alertnum=0).all().count()
            data_list.append(num)
        dict['secret_check_alert'] = data_list

        """
        已保密检查
        """
        data_list = []
        for x in date_hour:
            num = Docbmcheckresult.objects.filter(processtime__lte=x).all().count()
            data_list.append(num)
        dict['secret_check'] = data_list

        """
        隐写检查告警
        """
        data_list = []
        for x in date_hour:
            num = Picyxcheckresult.objects.filter(processtime__lte=x).all().count()
            data_list.append(num)
        dict['yx_check_alert'] = data_list

        """
        已隐写检查
        """
        data_list = []
        for x in date_hour:
            num = Docyxcheckresult.objects.filter(processtime__lte=x).all().count()
            data_list.append(num)
        dict['yx_check'] = data_list

        return dict

    def schoolar(self, day, name):
        """
        学术数据处理
        :param name:
        :return:字典
        """
        date_no_hour = [x[-5:] for x in self.g_get_no_hour_date(day)]
        date_hour = [x for x in self.g_get_hour_date(day)  ]
        dict = {}
        dict['date_no_hour'] = date_no_hour

        """
        万方数据
        """
        data_list = []
        for x in date_hour:
            num = Wanfangmetasource.objects.using("ScholarInfoBase").filter(crawltime__lte=x).all().count()
            data_list.append(num)
        dict['wanfang'] = data_list

        """
        ACM数据采集
        """
        data_list = []
        for x in date_hour:
            num = Acmmetasource.objects.using("ScholarInfoBase").filter(crawltime__lte=x).all().count()
            data_list.append(num)
        dict['acm'] = data_list

        """
        IEEE数据采集
        """
        data_list = []
        for x in date_hour:
            num = Ieeemetasource.objects.using("ScholarInfoBase").filter(crawltime__lte=x).all().count()
            data_list.append(num)
        dict['ieee'] = data_list

        """
        CNKI数据采集
        """
        data_list = []
        for x in date_hour:
            num = Cnkimetasource.objects.using("ScholarInfoBase").filter(crawltime__lte=x).all().count()
            data_list.append(num)
        dict['cnki'] = data_list


        return dict


    def baike(self, day, name):
        """
        百科数据处理
        :param name:
        :return:字典
        """
        date_no_hour = [x[-5:] for x in self.g_get_no_hour_date(day)]
        date_hour = [x for x in self.g_get_hour_date(day)  ]
        dict = {}
        dict['date_no_hour'] = date_no_hour

        """
        万方数据
        """
        data_list = []
        for x in date_hour:
            num = 1132716
            data_list.append(num)
        dict['baike'] = data_list

        return dict

    def homepage(self, day, name):
        """
        百科数据处理
        :param name:
        :return:字典
        """
        date_no_hour = [x for x in self.g_get_no_hour_date(day)]
        dict = {}
        dict['date_no_hour'] = [x[-5:] for x in self.g_get_no_hour_date(day)]
        uri = 'http://192.168.120.17:9206/datahouse/records/_search?pretty'
        """
        linkedIn数据
        """
        data_list = []
        for x in date_no_hour:
            num = linkedin.search(uri, "1900-12-12", x)
            data_list.append(num)
        dict['linkedin'] = data_list

        return dict

    def anwang(self, day, name):
        """
        百科数据处理
        :param name:
        :return:字典
        """
        date_no_hour = [x for x in self.g_get_no_hour_date(day)]
        dict = {}
        dict['date_no_hour'] = [x[-5:] for x in self.g_get_no_hour_date(day)]
        uri2 = 'http://192.168.120.17:9206/hiddenwebs_v2/hiddenwebpages/_search?pretty'

        """
        暗网数据
        """
        data_list = []

        for x in date_no_hour:
            num = tor.search(uri2, "1900-12-12", x)
            data_list.append(num)
        dict['anwang'] = data_list

        return dict

