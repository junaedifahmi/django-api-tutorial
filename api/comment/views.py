from blog.models import Comment

from rest_framework.viewsets import ModelViewSet

from .serializers import SerializerCommentModel


class ViewCommentModel(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = SerializerCommentModel


