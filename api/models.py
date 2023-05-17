from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    desciption = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    ###para ver en el panel de admin el nombre de la tarea
    def __str__(self):
        return self.title


