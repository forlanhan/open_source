# encoding:utf-8
from achievement_display.models import *
import time

class GetHighChartData:

    def g_get_no_hour_date(self, day):
        """
        :param day: 想要得到几天的时间
        :return: 只含年月日的日期
        """
        while day > 0:
            yield time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400 * (day - 1)))
            day = day - 1

    def g_get_hour_date(self, day):
        """
        :param day: 距离今天的时间间隔
        :return: 为一个字典 day['morning'] = "%Y-%m-d 00:00:00", day['night'] = "%Y-%m-d 23:59:59"
        """
        while day > 0:
            day_data = {}
            day_data['morning'] = time.strftime("%Y-%m-%d 00:00:00", time.localtime(time.time() - 86400 * (day-1)))
            day_data['night'] = time.strftime("%Y-%m-%d 23:59:59", time.localtime(time.time() - 86400 * (day-1)))
            yield day_data
            day = day - 1

    def wenku(self, num, class_name):

        if class_name == 'wenku_caiji':
            date_list = [x for x in self.g_get_no_hour_date(num) ]
            data_list = []
            dict = {}
            for x in date_list:
                number = Baidumetasource.objects.filter(crawltime__lte=x).all().count()
                data_list.append(number)
            dict['data_list'] = data_list
            dict['date_list'] = [x[-5:] for x in self.g_get_no_hour_date(num) ]
            return dict

        if class_name == 'secret_check_alert':
            date_hour_list = [x for x in self.g_get_hour_date(num) ]
            date_list = [x for x in self.g_get_no_hour_date(num) ]
            data_list = []
            dict = {}
            for x in date_hour_list:
                alert_num = Docbmcheckresult.objects.filter(processtime__lte=x['night']).exclude(alertnum=0).all().count()
                data_list.append(alert_num)
            dict['data_list'] = data_list
            dict['date_list'] = date_list
            return dict

        if class_name == 'secret_check':
            date_hour_list = [x for x in self.g_get_hour_date(num) ]
            data_list = []
            dict = {}
            for x in date_hour_list:
                alert_num = Docbmcheckresult.objects.filter(processtime__lte=x['night']).all().count()
                data_list.append(alert_num)
            dict['data_list'] = data_list
            return dict

        if class_name == 'yx_check':
            date_hour_list = [x for x in self.g_get_hour_date(num) ]
            data_list = []
            dict = {}
            for x in date_hour_list:
                alert_num = Docyxcheckresult.objects.filter(processtime__lte=x['night']).all().count()
                data_list.append(alert_num)
            dict['data_list'] = data_list
            return dict

        if class_name == 'yx_check_alert':
            date_hour_list = [x for x in self.g_get_hour_date(num) ]
            data_list = []
            dict = {}
            for x in date_hour_list:
                alert_num = Picyxcheckresult.objects.filter(processtime__lte=x['night']).all().count()
                data_list.append(alert_num)
            dict['data_list'] = data_list
            return dict


    def schoolar(self, num, class_name):

        if class_name == 'wanfang':
            date_list = [x for x in self.g_get_hour_date(num) ]
            data_list = []
            dict = {}
            for x in date_list:
                number = Wanfangmetasource.objects.using('ScholarInfoBase').filter(crawltime__lte=x['night']).count()
                data_list.append(number)
            dict['data_list'] = data_list
            dict['date_list'] = [x[-5:] for x in self.g_get_no_hour_date(num) ]
            return dict




if __name__ == "__main__":
    get_data = GetHighChartData()
    get_data.wenku(3, "wenku_caiji")