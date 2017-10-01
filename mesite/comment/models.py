#coding:utf-8
from django.db import models

# Create your models here.

class Comment(models.Model):
    name=models.CharField(max_length=100,verbose_name='用户名')
    email=models.EmailField(max_length=255,verbose_name='邮箱')
    url=models.URLField(blank=True,verbose_name='个人主页')
    text=models.TextField(verbose_name='评论')
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='发表时间')
    article=models.ForeignKey('blog.Article')

    def __unicode__(self):
        return self.text[:20]
    class Meta:
        verbose_name='博客评论'
        verbose_name_plural=verbose_name