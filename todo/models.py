from django.db import models

# Create your models here.
class TodoModel(models.Model):
    task_name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)