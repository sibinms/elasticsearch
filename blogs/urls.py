# urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArticleDocumentViewSet, ArticleSearch

router = DefaultRouter()
router.register(r'article', ArticleDocumentViewSet, basename='article')

urlpatterns = [
    path("article-search/", ArticleSearch.as_view())
]
urlpatterns += router.urls
