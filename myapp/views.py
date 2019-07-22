# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Students
from . serializers import StudentsSerializer
from django.http import HttpResponse
from rest_framework import viewsets

from collections import namedtuple
Timeline = namedtuple('Timeline', ('tweets', 'articles'))


# Create your views here.
class TimelineViewSet(APIView):
    """
    A simple ViewSet for listing the Students and Employees in your Timeline.
    """
    def list(self, request):
        timeline = Timeline(
            students = Students.objects.all(),
            employess = Employess.objects.all(),
        )
        serializer = CombinedSerializer(timeline)
        return Response(serializer.data)

