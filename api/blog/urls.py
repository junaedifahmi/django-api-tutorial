from django.conf.urls import url
from api.blog.views import (
    ViewArticleList,
    ViewArticleCreate,
    ViewArticleDetail,
    ViewArticleDelete,
    ViewArticleUpdate
)

urlpatterns = [
    url(r'^list/$', ViewArticleList.as_view(), name='all'),
    url(r'^create/$', ViewArticleCreate.as_view(), name='create'),
    url(r'^(?P<title>[\w-]+)/$', ViewArticleDetail.as_view(), name='detail'),
    url(r'^(?P<title>[\w-]+)/update/$', ViewArticleUpdate.as_view(), name='update'),
    url(r'^(?P<title>[\w-]+)/delete/$', ViewArticleDelete.as_view(), name='delete'),
]

