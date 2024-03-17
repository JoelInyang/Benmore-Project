from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')], default='todo')
    due_in = models.DurationField()  # Duration until the project is due
    tasks_total = models.PositiveIntegerField()  # Total number of tasks for the project
    tasks_completed = models.PositiveIntegerField(default=0)  # Number of completed tasks
    members = models.ManyToManyField('Member', related_name='projects', blank=None, null=True)

class Member(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    
