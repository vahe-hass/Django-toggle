# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]


htmx_urlpatterns = [

    path('toggle_input', views.toggle_input, name='toggle-input')
]

urlpatterns += htmx_urlpatterns
