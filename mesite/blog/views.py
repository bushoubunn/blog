#_*_coding:utf-8_*_
from django.shortcuts import render,get_object_or_404
from blog.models import *
# Create your views here.
from django.http import HttpResponse
from comment.forms import CommentForm
import markdown
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q


def index(request):
	artcile_list=Article.objects.all()
	paginator=Paginator(artcile_list,2)
	page=request.GET.get('page')
	try:
		articles=paginator.page(page)
	except PageNotAnInteger:
		articles=paginator.page(1)
	except EmptyPage:
		articles=paginator.page(paginator.num_pages)
	context = {'title': u'我的博客首页', 'artcile_list': articles}
	return render(request,'blog/index.html',context)

def detail(request,pk):
	article=get_object_or_404(Article,pk=pk)
	article.increase_views()
	article.body=markdown.markdown(article.body,extension=['markdown.extensions.extra',
														   'markdown.extensions.codehilite',
														   'markdown.extensions.toc'])
	form=CommentForm()
	comment_list=article.comment_set.all()
	context={
		'article':article,
		'form':form,
		'comment_list':comment_list
	}
	return render(request,'blog/detail.html',locals())

def archives(request,year,month):
	artcile_list=Article.objects.filter(create_time__year=year,
										create_time__month=month).order_by('-create_time')
	return render(request,'blog/index.html',locals())

def category(request,pk):
	categories=get_object_or_404(Category,pk=pk)
	artcile_list=Article.objects.filter(category=categories).order_by('-create_time')

	return render(request,'blog/index.html',locals())

def tag(request,pk):
	tags=get_object_or_404(Tag,pk=pk)
	artcile_list=tags.article_set.all()

	return render(request,'blog/index.html',locals())

def search(request):
	q=request.GET.get('q')
	error_msg=''
	if not q:
		error_msg='请输入关键字'
		return render(request,'blog/index.html',{'error_msg':error_msg})
	artcile_list=Article.objects.filter(Q(title__contains=q)|Q(body__contains=q))
	return render(request,'blog/index.html',locals())