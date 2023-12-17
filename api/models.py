from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __self__(self):
        return self.title