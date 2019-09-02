from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class SerializerCommentModel(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
