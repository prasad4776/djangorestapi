# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length = 50)
    dept = models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Employees(models.Model):
    e_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.e_name


    

    