from django.db import models
from django.db.models import CharField, DateField, ForeignKey, Model
from django.contrib.auth.models import User
from autoslug import AutoSlugField


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True)
    slug = AutoSlugField(populate_from='title',blank=True)
    video = models.FileField(upload_to='videos/',blank=True)
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'