from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = (
            'id',
            'todo',
            'slug',
            'user',
            'finished',
            'deleted',
            'created',
            'modified',
        )
