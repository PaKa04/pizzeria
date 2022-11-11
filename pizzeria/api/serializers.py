from rest_framework.serializers import ModelSerializer
from app.models import Post
from slugify import slugify


class PostSerializer(ModelSerializer):

    def create(self, validated_data):
        post = Post(**validated_data | {'slug': slugify(validated_data.get('title') + validated_data.get('subtitle'))})
        post.save()
        return post

    class Meta:
        model = Post
        fields = {'id', 'title', 'subtitle', 'first_text', 'image_of_post1', 'second_text', 'author'}
