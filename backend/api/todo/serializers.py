from rest_framework.serializers import ModelSerializer
from todo.models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["user_id","user", "id", "title", "completed"]
        extra_kwargs = {
            "user_id": {"read_only": True},
            "user": {"write_only": True},
        }