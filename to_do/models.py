from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)

class UnActiveManager(models.Manager):
    def get_queryset(self):
        return super(UnActiveManager, self).get_queryset().filter(active=False)

class Todo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, db_index=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    undone = ActiveManager()
    done = UnActiveManager()

    class Meta:
        ordering = ('-created',)
        unique_together = ['title', 'created']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Todo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('to_do:todo_detail', args=[self.created.year,
                                              self.created.month,
                                              self.created.day,
                                              self.slug])