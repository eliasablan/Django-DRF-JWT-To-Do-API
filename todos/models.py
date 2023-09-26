from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    todo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    finished = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.todo)
        super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return self.todo