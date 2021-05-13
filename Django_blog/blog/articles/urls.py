from django.conf.urls import url
from django.urls import path
from .import views

app_name='articles'

urlpatterns = [
    url(r'^$', views.article_list),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='detail'),
]
