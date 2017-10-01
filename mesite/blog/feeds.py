#coding:utf-8

from django.contrib.syndication.views import Feed

from .models import Article

class AllArticlesRssFeed(Feed):

    title="Django 博客测试"
    link='/'
    description="Django 博客文章测试"

    def items(self):

        return Article.objects.all()
    def item_title(self, item):
        return '[%s]%s'%(item.category,item.title)
    def item_description(self, item):
        return item.body