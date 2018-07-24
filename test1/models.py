from django.db import models

# Create your models here.

from django.db import models


class Snippet(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)
    award = models.TextField()
    address = models.TextField()
    status = models.CharField(max_length=100)

    class Meta:
        ordering = ('time',)
