#_*_coding:utf-8_*_
import markdown
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags


# Create your models here.

#分类
class Category(models.Model):
	name=models.CharField(max_length=100,verbose_name='分类名称')

	class Meta:
		verbose_name='分类'
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return self.name
#标签
class Tag(models.Model):
	name=models.CharField(max_length=100)

	class Meta:
		verbose_name='标签'
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return self.name
#文章
class Article(models.Model):

	title=models.CharField(max_length=70,verbose_name='文章标题')
	body=models.TextField(verbose_name='文章内容')
	create_time=models.DateTimeField(verbose_name='发布时间')
	modified_time=models.DateTimeField(verbose_name='修改时间')
	excerpt=models.CharField(max_length=200,blank=True,verbose_name='文章摘要')
	category=models.ForeignKey(Category,verbose_name='文章分类')
	tags=models.ManyToManyField(Tag,blank=True,verbose_name='文章标签')
	author=models.ForeignKey(User,verbose_name='文章作者')
	views=models.PositiveIntegerField(default=0)
	class Meta:
		verbose_name='文章'
		verbose_name_plural=verbose_name
		ordering=['-create_time']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	def increase_views(self):
		self.views+=1
		self.save(update_fields=['views'])

	def save(self,*args,**kwargs):
		
		if not self.excerpt:
			
			md=markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite'
			])
			self.excerpt=strip_tags(md.convert(self.body))[:54]
			
		super(Article, self).save(*args,**kwargs)
			






