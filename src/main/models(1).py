# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField('Your First and Last Name', max_length=30, blank=False)
    question = models.TextField('Your Question', max_length=2000, blank=False)
    
    def __str__(self):
        return self.name