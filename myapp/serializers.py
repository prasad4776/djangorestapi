from rest_framework import serializers
#from rest_framework import Students
from . models import Students,Employees


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees

class CombinedSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many = True)
    employees = EmployeeSerializer(many = True)

