from django.db import models

class SystemInstructions(models.Model):
    name = models.CharField(max_length=5000)
    instructions = models.TextField()

    def __str__(self):
        return self.name