from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    