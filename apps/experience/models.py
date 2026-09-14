from django.db import models


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    date_range = models.CharField(max_length=100, help_text='e.g. May 2025 — Present')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.role} — {self.organization}'


class ExperienceHighlight(models.Model):
    experience = models.ForeignKey(Experience, related_name='highlights', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:60]
