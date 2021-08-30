from django.contrib import admin

from blog.models import Category, Article


admin.site.register(Category)
admin.site.register(Article)
