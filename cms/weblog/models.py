import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown import markdown
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
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, "Live"),
        (DRAFT_STATUS, "Draft"),
        (HIDDEN_STATUS, "Hidden"),
    )

    # Core Fields
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True, help_text="A small portion of text to show as a preview on the main page. Can be blank")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Metadata
    slug = models.SlugField(unique_for_date="pub_date")
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    # Categorization
    categories = models.ManyToManyField(Category)
    tags = TagField()

    # Fields to store generated HTML
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return ('weblog_entr_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug })