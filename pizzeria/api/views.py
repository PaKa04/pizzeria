from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer
from app.models import Post


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
