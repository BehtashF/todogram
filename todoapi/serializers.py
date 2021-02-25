from rest_framework import serializers
from todo.models import Task





class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'created_at']
        # extra_kwargs = {
        #     'user': {'write_only': True}
        # }