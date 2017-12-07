# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from .models import Newspaper
from .forms import QuestionForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def bio(request):
    return render(request, 'biography.html')

def ask(request):
    form = QuestionForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Your question has been recorded. You should recieve an email from Leo with the answer. Thank you!')
        return HttpResponseRedirect('/')
    
    return render(request, 'ask.html', {'form': form})

def learnmore(request):
    return render(request, 'campaigninfo.html')

def news(request):
    return render(request, 'news.html', {'newspapers': Newspaper.objects.all()})