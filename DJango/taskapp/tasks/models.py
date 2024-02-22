from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(
        'TaskGroup',        #to be more specific
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    def __str__(self):
        return '{} due on {}'.format(self.name, self.due_date)
    
    def get_absolute_url(self):
        #return /task/name
        return reverse('task-detail', args=[self.pk])        #self.pk is primary key (int no.)
    
    @property
    def is_due(self):       #access using instance.is_due
        return datetime.now() >= self.due_date
    #add meta data about the model
    class Meta:
        ordering = ['due_date']                 #how to order by default the model (default = follow primary key); ascending = positive (no need to put +       sign), descending = negative (e.g. '-due_date')
        unique_together = ['due_date', 'name']  #cant have the same due date and name; possible 2d array (e.g. [['due_date', 'name'], []])
        verbose_name = 'Task'                   #django uses model name by default; plural is name+s
        verbose_name_plural = 'Tasks'