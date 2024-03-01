from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import ArticleDocument


class ArticleSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        fields = '__all__'
