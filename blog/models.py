from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
