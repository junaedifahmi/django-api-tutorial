from django.conf.urls import url, include

urlpatterns = [
    url(r'^blog/', include('api.blog.urls'), name='blog-api'),
    url(r'^comment/', include('api.comment.urls'), name='comment-api')
]
