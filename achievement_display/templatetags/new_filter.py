# ecoding:utf-8
from django import template
from achievement_display.models import *


register = template.Library()

@register.filter(name="workfor")
def workfor(string):
    """
    对数据进行提取
    """
    res = string.split('|')
    if len(res) > 1:
        return res[1]
    else:
        return "暂无"

@register.filter(name="find_name")
def find_name(string):
    """
    通过ID查找出文档名称
    :param string: 文档ID
    :return: 文档名称
    """
    res = Baidumetasource.objects.get(id=string)
    if res:
        return res.filename
    else:
        return "无"

@register.filter(name="sort")
def sort(string, sort):
    """
    替换路径中sort参数得值
    :param string: 要替换得值
    :return: 路径
    """
    str = "/search?"
    for key, value in string.items():
        if key == "sort":
            str += key + '=' + sort + '&'
        else:
            str += key + '=' + value + '&'
    return str
