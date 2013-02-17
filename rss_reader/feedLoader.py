from rss_reader.models import FeedEntry
from django.db import IntegrityError
import feedparser


class FeedLoader:
    def __init__(self, url):
        self.url = url

    def pull_feed(self, posts_to_show=50):
        feed = feedparser.parse(self.url)
        self.fillHeader(feed)
        if posts_to_show > feed['entries'].__len__():
            posts_to_show = feed['entries'].__len__()
        for i in range(posts_to_show):
            try:
                FeedEntry(
                    post_id=feed['entries'][i].id,
                    author=feed['entries'][i].author,
                    title=feed['entries'][i].title,
                    body=feed['entries'][i].content[0].value,
                    link=feed['entries'][i].link,
                    timestamp=feed['entries'][i].updated
                ).save()
            except IntegrityError:
                pass

    def fillHeader(self, feed):
        self.title = feed['feed'].title
        self.subtitle =  feed['feed'].subtitle