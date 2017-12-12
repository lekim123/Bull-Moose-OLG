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
    name = models.CharField(max_length=50, blank=False)
    text = models.TextField(max_length=2500, blank=False)
    
    def __str__(self):
        return self.name
    
class Newspaper(models.Model):
    name = models.CharField(max_length=50, blank=False)
    articles = models.ManyToManyField(Article)
    
    def __str__(self):
        return self.name
    
class IPAddress(models.Model):
    ip = models.GenericIPAddressField()
    
    def __str__(self):
        return self.ip + " is let into the admin site."
    