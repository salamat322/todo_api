from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100)
    made = models.TimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})