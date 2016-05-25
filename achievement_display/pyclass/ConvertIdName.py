# encoding: utf-8
from achievement_display.models import *

class ConvertIdName:

    def convet_id_name(self, string):
        """
        转换姓名
        :param string:
        :return:
        """
        try:
            res = Baidumetasource.objects.get(id=string)
            if res:
                return res.filename
            else:
                return "无"

        except:
            return string
