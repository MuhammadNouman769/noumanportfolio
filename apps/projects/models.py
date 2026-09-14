from django.db import models


class Project(models.Model):
    STATUS_LIVE = 'live'
    STATUS_PROGRESS = 'progress'
    STATUS_DEPLOYMENT = 'deployment'
    STATUS_CHOICES = [
        (STATUS_LIVE, 'Live'),
        (STATUS_PROGRESS, 'In Progress'),
        (STATUS_DEPLOYMENT, 'Deployment Phase'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PROGRESS)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=True, help_text='Show on the homepage highlights.')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text