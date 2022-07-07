# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    seo = models.BooleanField(default=False)
    content_marketing = models.BooleanField(default=False)
    web_dev = models.BooleanField(default=False)
    ux_design = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
