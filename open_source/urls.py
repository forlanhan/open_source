"""open_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.conf.urls import url, include
from achievement_display.views import *
from achievement_display.pyclass.DataTable import OrderListJson
from achievement_display.pyclass.BmCheckAlert import BmCheckAlert
from achievement_display.pyclass.BmCheck import BmCheck
from achievement_display.pyclass.YxCheck import YxCheck
from achievement_display.pyclass.YxCheckAlert import YxCheckAlert

# urlpatterns = [
#     url(r'^data/$', OrderListJson.as_view(), name='order_list_json'),
#     url(r'^test/$', test),
#     url(r'^datatable/$', datatable),
# ]
#
# """
#achievement_display
urlpatterns = patterns('achievement_display.views',
                       (r'^index/?$', 'index'),
                       (r'^highchart/?$', 'highchart'),
                       (r'wenku/?$', 'wenku'),
                       (r'datatables_iframe/?$', 'datatables_iframe'),
                       (r'search/?$', 'search'),
                       (r'ajax_page/?$', 'ajax_page'),
                       (r'force/?$', 'force'),
                       (r'force_open/?$', 'force_open'),
                       (r'test/?$', 'test'),
                       (r'convert_id_name/?$', 'convert_id_name'),
                       (r'^data/?$', OrderListJson.as_view()),
                       (r'^datatable_1/?$', BmCheckAlert.as_view()),
                       (r'^datatable_2/?$', BmCheck.as_view()),
                       (r'^datatable_3/?$', YxCheck.as_view()),
                       (r'^datatable_4/?$', YxCheckAlert.as_view()),
                       (r'search2/?$', 'search2'),
                       (r'card_get_res/?$', 'card_get_res'),
                       (r'get_node_info/?$', 'get_node_info'),
                       (r'ajax_agg/?$', 'ajax_agg'),
                       (r'', 'index')
                       )






