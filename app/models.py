from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100000)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name