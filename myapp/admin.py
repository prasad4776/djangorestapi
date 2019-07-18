# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#djangoprasad 
from django.contrib import admin
from . import models
from models import Students


# Register your models here.
admin.site.register(Students)