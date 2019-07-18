# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Students
from . serializers import StudentsSerializer
from django.http import HttpResponse


# Create your views here.
class StudentsList(APIView):


    def get(self,request):
        students1 = Students.objects.all()
        serializer = StudentsSerializer(students1,many = True)
    
        return Response(serializer.data)

