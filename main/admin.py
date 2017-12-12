# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question, Article, Newspaper

class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)

class NewspaperAdmin(admin.ModelAdmin):
    class Meta:
        model = Newspaper

admin.site.register(Newspaper, NewspaperAdmin)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)