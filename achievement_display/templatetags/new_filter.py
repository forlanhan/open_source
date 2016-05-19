# ecoding:utf-8
from django import template
from achievement_display.models import *
import base64
import re

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

