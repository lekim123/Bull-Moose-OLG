# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField('Your First and Last Name', max_length=30, blank=False)
    question = models.TextField('Your Question', max_length=2000, blank=False)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=40, blank=False)
    summary = models.TextField(max_length=500, blank=False)
    text = models.TextField(max_length=5000, blank=False)
    datePosted = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Newspaper(models.Model):
    name = models.CharField(max_length=40, blank=False)
    articles = models.ManyToManyField(Article)
    
    def get_latest_post(self):
        return self.articles.all().latest('datePosted')
    
    def latest(self):
        return self.articles.order_by('-datePosted')
    
    def sort_articles(self):
        s = []
        i = []
        idx = 0
        for n in self.latest():
            if idx == 3:
                s.append(i)
                i = []
                idx = 0
            i.append(n)
            idx += 1
        s.append(i)
        return s
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def sort_self():
        s = []
        i = []
        idx = 0
        for n in Newspaper.objects.all():
            if idx == 3:
                s.append(i)
                i = []
                idx = 0
            i.append(n)
            idx += 1
        s.append(i)
        return s
    