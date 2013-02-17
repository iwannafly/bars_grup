from django.template import loader, Context
from django.http import HttpResponse
from rss_reader.feedLoader import FeedLoader
from rss_reader.models import BlogPost


def main(request):
    feedLoader = FeedLoader('http://rss1.smashingmagazine.com/feed/')#'http://rss1.smashingmagazine.com/feed/')
    feedLoader.pull_feed(10)
    posts = BlogPost.objects.all()
    t = loader.get_template("main.html")
    c = Context({'feed': feedLoader, 'posts': posts})
    return HttpResponse(t.render(c))

