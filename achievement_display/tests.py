# encoding:utf-8
from django.shortcuts import render
from achievement_display.models import *
from django.http import HttpResponse, HttpResponseRedirect
from achievement_display.pyclass.GetHighChartData import GetHighChartData
from achievement_display.pyclass.Search import Search
import time
import linkedin
import tor
import json
import types


from achievement_display.models import *
num = Docbmcheckresult.objects.all().count()
print num

