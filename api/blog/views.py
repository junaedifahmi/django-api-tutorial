from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView
)

from api.blog.serializers import (
    SerializerArticleDetail,
    SerializerArticleCreateUpdate,
)

from blog.models import Articles


class ViewArticleCreate(CreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = SerializerArticleCreateUpdate


class ViewArticleDetail(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = SerializerArticleCreateUpdate
    lookup_field = 'title'


class ViewArticleUpdate(UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = SerializerArticleCreateUpdate
    lookup_field = 'title'


class ViewArticleDelete(DestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = SerializerArticleDetail
    lookup_field = 'title'


class ViewArticleList(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = SerializerArticleDetail

