from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    

    def _str_(self):
        return self.title