"""Leonard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import ask, bio, home, learnmore, news

admin.site.site_header = 'Llama Party Administration'
admin.site.site_title = 'Llama Party Administration'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^bio/$', bio, name='bio'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^campaign/$', learnmore, name='campaign'),
    url(r'^news/$', news, name='news'),
    url(r'^admin/', admin.site.urls),
]
