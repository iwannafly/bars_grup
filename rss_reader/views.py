# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.http import HttpResponse
from rss_reader.feedLoader import FeedLoader
from rss_reader.models import FeedEntry


def main(request):
    # создаём объект загрузчика фидов
    feedLoader = FeedLoader('http://rss1.smashingmagazine.com/feed/')
    # парсим и добавляем в БД новые записи
    feedLoader.fetchFeeds(10)
    # получаем все записи БД
    posts = FeedEntry.objects.all()
    # загружаем и заполняем шаблон главной страницы
    t = loader.get_template("main.html")
    c = Context({'feed': feedLoader, 'posts': posts})
    return HttpResponse(t.render(c))


def showFullInfo(request, poll_id):
    # получаем объект с переданым при переходе по ссылке id
    post = FeedEntry.objects.get(id = poll_id)
    # загружаем и заполняем шаблон страницы полной информации
    t = loader.get_template("full_info.html")
    c = Context({'post': post})
    return HttpResponse(t.render(c))
