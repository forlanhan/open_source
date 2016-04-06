#!encoding: utf-8
from django.shortcuts import render
from achievement_display.models import *
from django.http import HttpResponse
import time
import linkedin

# Create your views here.

def index(request):
    content = IpWrite.objects.all().using('kankan').count()
    return HttpResponse(content)

