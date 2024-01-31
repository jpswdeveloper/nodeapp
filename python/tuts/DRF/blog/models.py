from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

# Create your models here.


# Post category
# Use can post a post which has categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    # Custom def to access all published data
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    # Enums
    options = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    # One to One with category if categories data is deleted it also deletes all the posts related to category
    categories = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)

    # Handle user status data
    status = models.CharField(max_length=10, choices=options, default="published")

    # add custom managers and default manager
    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title

    # Custom ordering
    class Meta:
        ordering = ["-published"]
