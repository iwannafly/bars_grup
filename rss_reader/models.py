# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class FeedEntry(models.Model):
    # уникальность поля защищает от повторной загрузки того же фида
    post_id = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    body = models.TextField()
    link = models.URLField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class FeedEntryAdmin(admin.ModelAdmin):
    # конфигурирует отображение в админке
    list_display = ('title', 'author', 'timestamp')

# регистрируем в админке
admin.site.register(FeedEntry, FeedEntryAdmin)
