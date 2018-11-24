"""app URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^about$', views.aboutpage),
    url(r'^api/create_issue$', views.api_create_issue),
    url(r'^create_issue$', views.create_issue),
    url(r'^api/save_comment$', views.create_comment),
    url(r'^issues$', views.view_issues),
    url(r'^admin/', admin.site.urls),
    url(r'^issue/(?P<uuid>[0-9a-f-]+)', views.view_issue),
    url(r'^', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^', include('social_django.urls', namespace='social')),
]
