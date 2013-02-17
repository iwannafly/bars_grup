from django.template import loader, Context
from django.http import HttpResponse
from rss_reader.models import BlogPost


def  main(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("main.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))