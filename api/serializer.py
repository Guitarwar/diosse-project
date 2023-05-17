from rest_framework import serializers
from .models import Task

class TaskSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'title', 'description', 'don')
        fields = '__all__'

