from django.contrib import admin
from models import Tag,Category,Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','author']
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)