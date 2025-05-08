from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'

