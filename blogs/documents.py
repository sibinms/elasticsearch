from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Article


@registry.register_document
class ArticleDocument(Document):
    """
    uuid Field:
        This field corresponds to the uuid field in your Django model (Article).
        fields.KeywordField is used for keyword fields in Elasticsearch,
        which are suitable for storing identifiers like UUIDs.
        Keyword fields are not analyzed, meaning they are treated as single terms.
        The attr='uuid' parameter specifies that the data for this field will
         be taken from the uuid attribute of the Article model.

    resume_text Field:
        This field corresponds to the resume_text field in your Django model.
        fields.TextField is used for text fields in Elasticsearch. Text fields are typically analyzed,
        meaning they are broken into individual terms during indexing.
        The attr='content' parameter specifies that the data for this field will be
        taken from the resume_text attribute of the Article model.
    """
    class Index:
        name = 'article_index'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    uuid = fields.KeywordField(attr='uuid')
    title = fields.TextField(attr='title')
    content = fields.TextField(attr='content')

    class Django:
        model = Article
