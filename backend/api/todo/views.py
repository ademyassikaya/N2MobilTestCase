from rest_framework.viewsets import ModelViewSet
from todo.models import Todo
from api.todo.serializers import TodoSerializer


class TaskViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer