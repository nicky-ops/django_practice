from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum 250 characters")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated rom title. Must be unique.")
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class Entry(models.Model):
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField()