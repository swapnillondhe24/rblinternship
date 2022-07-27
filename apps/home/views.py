# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home import forms
from Data_fetch_python.scrapeBot import scrapeBot
from django.shortcuts import render
import pandas as pd


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
def search(request):
    context = {}
    if request.method == 'POST':
        context['segment'] = request.POST.get('srch')
        print(context['segment'])
        
        obj = scrapeBot(context['segment'])
        df,name = obj.getData()
        context['df'] = df
        context['name'] = name.upper()
        for i in df:
            context[i] = df[i]
        return render(request, 'home/tables.html', context)
    
def search_table(request):
    html_template = loader.get_template('home/tables.html')
    context = {}
    return HttpResponse(html_template.render(context, request))
