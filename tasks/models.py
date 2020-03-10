from django.db import models
from django.urls import reverse

from tags.models import Tag


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    made = models.TimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})