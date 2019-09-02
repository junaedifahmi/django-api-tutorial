from rest_framework.serializers import ModelSerializer

from blog.models import Articles


class SerializerArticleDetail(ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'


class SerializerArticleCreateUpdate(ModelSerializer):
    class Meta:
        model = Articles
        fields = ['title', 'content']
