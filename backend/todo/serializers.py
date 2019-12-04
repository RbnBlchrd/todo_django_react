from rest_framework import serializers
from .models import Todo


# We need serializers to convert model instances to JSON so that the frontend
# can work with the received data easily.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # specify fields we want to keep
        fields = ('id', 'title', 'description', 'completed')
