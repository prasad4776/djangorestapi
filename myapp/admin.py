# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#djangoprasad 
from django.contrib import admin
from . models import Students,Employees


# Register your models here.
admin.site.register(Students)
admin.site.register(Employees)