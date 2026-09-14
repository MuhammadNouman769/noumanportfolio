from django.db import models


class Profile(models.Model):
    """Singleton-style bio block shown on the About page. Only one row is expected."""
    headline = models.CharField(max_length=150, default='Backend Engineer')
    bio_paragraph_1 = models.TextField()
    bio_paragraph_2 = models.TextField(blank=True)
    bio_paragraph_3 = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.headline


class Education(models.Model):
    degree = models.CharField(max_length=120)
    institution = models.CharField(max_length=200)
    date_range = models.CharField(max_length=50, help_text='e.g. 2020 — 2024')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.degree} — {self.institution}'
