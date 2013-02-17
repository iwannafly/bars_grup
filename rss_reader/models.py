from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    post_id = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    body = models.TextField()
    link = models.URLField()
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp')


class Meta:
    ordering = ('-timestamp',)


admin.site.register(BlogPost, BlogPostAdmin)
