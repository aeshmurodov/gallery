from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True, editable=False)