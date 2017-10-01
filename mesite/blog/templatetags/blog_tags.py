#coding:utf-8
from ..models import Article,Category,Tag
from django import template
from django.db.models.aggregates import Count

register=template.Library()

#获取最近的文章,数目是4
@register.simple_tag
def get_recent_articles(num=4):
    return Article.objects.all().order_by('-create_time')[:4]

#归档
@register.simple_tag
def archives():
    return Article.objects.dates('create_time','month',order='DESC')

#分类
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)

#标签
@register.simple_tag()
def get_tags():
    return Tag.objects.all()