from elasticsearch_dsl import Q
from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .documents import ArticleDocument
from .serializers import ArticleSerializer


class ArticleSearch(APIView):
    """
    Elasticsearch uses the Levenshtein edit distance to implement fuzzy matching in its queries.
    The Levenshtein distance is a measure of the similarity between two strings by calculating the minimum number of
    single-character edits (insertions, deletions, or substitutions) required to change one string into the other.
    """
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def _generate_q_expression(self, query):
        # Use a single Q object for both title and content
        return Q("multi_match", query=query, fields=["title", "content"], fuzziness="auto")

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get("search")
        try:
            q = self._generate_q_expression(search_query)
            search = self.document_class.search().query(q)
            results = search.to_queryset()
            serialized_data = self.serializer_class(results, many=True).data
            return Response(serialized_data)
        except Exception as e:
            # Handle exceptions, e.g., when there's no data or Elasticsearch is unreachable
            return Response({"error": str(e)}, status=500)


class ArticleDocumentViewSet(BaseDocumentViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    document = ArticleDocument
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilterBackend]
    search_fields = ['title', 'content']
