from django.db import models
from user.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title