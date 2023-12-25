from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Todo title : {self.title}'
    
    class Meta:
        ordering =['created_at']
        db_table = 'TodoList'