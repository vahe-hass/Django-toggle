# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Service


# refactor this by reducing 2 queries to 1. eg(service.objects.filter & get)
@login_required(login_url="/login/")
def toggle_input(request):
    current_user = request.user
    current_user_id = current_user.id
    if Service.objects.filter(user_id=current_user_id).exists():
        current_user_service = Service.objects.get(user_id=current_user_id)
        service_state = current_user_service.seo
        if service_state == True:
            current_user_service.seo = False
            current_user_service.save()
        else:
            current_user_service.seo = True
            current_user_service.save()

    return HttpResponse("")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')


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

        if load_template == 'tables.html':
            services = Service.objects.all()
            context['services'] = services
            html_template = loader.get_template('home/' + load_template)
            return HttpResponse(html_template.render(context, request))

        if load_template == 'profile.html':
            current_user = request.user
            current_user_id = current_user.id
            user_services_query = Service.objects.filter(user_id=current_user_id)
            # checking Service Query
            if len(user_services_query) == 0:
                print(" NOTE!! Admin & Staff service query List is empty **")
                html_template = loader.get_template('home/' + load_template)
                return HttpResponse(html_template.render(context, request))
            else:
                user_services = user_services_query[0]
                context['user_services'] = user_services
                context['checked'] = 'checked'
                html_template = loader.get_template('home/' + load_template)


        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
        pass

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
