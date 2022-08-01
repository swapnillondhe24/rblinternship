# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf.urls import url, include

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('search_res', views.search, name='search'),
    path('table', views.search_table, name='serach_table'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
