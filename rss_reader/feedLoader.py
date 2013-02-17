# -*- coding: utf-8 -*-
from rss_reader.models import FeedEntry
from django.db import IntegrityError
# решил не изобретать велосипед - парсим фиды либой feedparser
import feedparser


class FeedLoader:
    # конструктор, устанавливает url с которого загружаем фиды
    def __init__(self, url):
        self.url = url

    # получает фиды, парсит и создает записи в БД
    # по дефолту грузим 20 последних
    def fetchFeeds(self, posts_to_show=20):
        feed = feedparser.parse(self.url)
        self.fillHeader(feed)
        # проверяем есть ли в фид листе искомое количество фидов,
        # если их меньше чем просит загрузить вьюха - грузим столько, сколько есть
        if posts_to_show > feed['entries'].__len__():
            posts_to_show = feed['entries'].__len__()
        # заполняем БД
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
            # вылетит если запись в базе уже есть
            except IntegrityError:
                # так обрабатывать исключения конечно нельзя)
                pass

    # заполняет информацию об источнике фидов
    def fillHeader(self, feed):
        self.title = feed['feed'].title
        self.subtitle =  feed['feed'].subtitle