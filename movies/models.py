from django.db import models
from actors.models import Actor
from genres.models import Genre

class Movies(models.Model):
    title =  models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

