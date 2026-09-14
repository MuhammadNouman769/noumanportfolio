from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=220, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
