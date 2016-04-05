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
'''
urlpatterns = [
    url(r'^hello/$',hello),
    url(r'^testdb/$', testdb),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/$', Test.admin),
]
'''
#achievement_display
urlpatterns = patterns('achievement_display.views',
                       (r'^index/$', 'index'),
                       )




