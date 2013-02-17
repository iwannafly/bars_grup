import datetime
from django.db import models
from django.contrib import admin
import feedparser


class BlogPost(models.Model):
    post_id = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    #author_uri = models.URLField()
    title = models.CharField(max_length=250)
    body = models.TextField()
    link = models.URLField()
    timestamp = models.DateTimeField()

    def pull_feed(self, feed_url, posts_to_show=5):
        feed = feedparser.parse(feed_url)
        posts = []

        for i in range(posts_to_show):
            posts.append({
                'id': feed['entries'][i].id,
                'author': feed['entries'][i].author,
                'title': feed['entries'][i].title,
                'summary': feed['entries'][i].content[0].value,
                'link': feed['entries'][i].link,
                'date': feed['entries'][i].updated,
            })

            try:
                BlogPost(
                    post_id=feed['entries'][i].id,
                    author=feed['entries'][i].author,
                    title=feed['entries'][i].title,
                    body=feed['entries'][i].content[0].value,
                    link=feed['entries'][i].link,
                    timestamp=feed['entries'][i].updated
                ).save()
            except:
                pass
        return {'posts': posts}


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
