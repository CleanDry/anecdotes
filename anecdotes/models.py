from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anecdote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    anecdote_text = models.CharField(max_length=400)

    def __str__(self):
        return self.anecdote_text