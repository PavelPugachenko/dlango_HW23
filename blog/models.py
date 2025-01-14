from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='blog_previews', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
