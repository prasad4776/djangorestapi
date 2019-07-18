from rest_framework import serializers
#from rest_framework import Students
from . models import Students


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields  = '__all__'
