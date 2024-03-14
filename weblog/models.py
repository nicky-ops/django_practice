from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title