from django.db import models
from django.contrib import admin
from django.db.models import permalink


class FeedEntry(models.Model):
    post_id = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    body = models.TextField()
    link = models.URLField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

    @permalink
    def get_absolute_url(self):
        return ("get_hostname/",
            None, {'object_id': self.id})


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp')

admin.site.register(FeedEntry, BlogPostAdmin)
