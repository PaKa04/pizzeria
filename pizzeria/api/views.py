from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from app.models import Post, Pizza, Product, Category



# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer


class PostApiView(View):

    def get(self, request: HttpResponse, post_id=None):
        if not post_id:
            posts = Post.objects.all().filter(is_published=True)
            data = {}
            for post in posts:
                data[str(post.id)] = {
                    'title': post.title,
                    'subtitle': post.subtitle,
                    'first_text': post.first_text,
                    'image_of_post1': post.image_of_post1.url,
                    'second_text': post.second_text,
                    'author': post.author
                }
            return JsonResponse(data=data)
        else:
            post = Post.objects.filter(pk=int(post_id))
            if post:
                post = post[0]
                post = {
                    'title': post.title,
                    'subtitle': post.subtitle,
                    'first_text': post.first_text,
                    'image_of_post1': post.image_of_post1.url,
                    'second_text': post.second_text,
                    'author': post.author
                }
                return JsonResponse(data=post)
            else:
                return JsonResponse(data={'status': 404, 'detail': f'post {post_id} does not exist'}, status=404)


class CategoryApiView(View):

    def get(self, request: HttpResponse, category_id=None):
        if not category_id:
            posts = Category.objects.all().filter(is_published=True)
            data = {}
            for post in posts:
                data[str(post.id)] = {
                    'name': post.name,
                    'descr': post.descr
                }
            return JsonResponse(data=data)
        else:
            post = Category.objects.filter(pk=int(category_id))
            if post:
                post = post[0]
                post = {
                    'name': post.name,
                    'descr': post.descr
                }
                return JsonResponse(data=post)
            else:
                return JsonResponse(data={'status': 404, 'detail': f'category {category_id} does not exist'}, status=404)


class ProductApiView(View):

    def get(self, request: HttpResponse, category_id,  product_id=None, ):
        if not product_id:
            posts = Product.objects.all().filter(is_published=True, category_id=int(category_id))
            data = {}
            for post in posts:
                data[str(post.id)] = {
                    'title': post.title,
                    'descr': post.descr,
                    'price': post.price,
                    'image': post.image.url if post.image else 'Null'
                }
            return JsonResponse(data=data)
        else:
            post = Product.objects.filter(pk=int(product_id))
            if post:
                post = post[0]
                post = {
                    'title': post.title,
                    'descr': post.descr,
                    'price': post.price,
                    'image':  post.image.url if post.image else 'Null'
                }
                return JsonResponse(data=post)
            else:
                return JsonResponse(data={'status': 404, 'detail': f'product {product_id} does not exist or wrong categori id {category_id}'}, status=404)


class PizzaApiView(View):

    def get(self, request: HttpResponse, pizza_id=None):
        if not pizza_id:
            posts = Pizza.objects.all().filter(is_published=True)
            data = {}
            for post in posts:
                data[str(post.id)] = {
                    'title': post.name,
                    'descr': post.descr,
                    'price': post.price,
                    'image': post.image.url if post.image else 'Null'
                }
            return JsonResponse(data=data)
        else:
            post = Pizza.objects.filter(pk=int(pizza_id))
            if post:
                post = post[0]
                post = {
                    'title': post.name,
                    'descr': post.descr,
                    'price': post.price,
                    'image': post.image.url if post.image else 'Null'
                }
                return JsonResponse(data=post)
            else:
                return JsonResponse(data={'status': 404, 'detail': f'product {pizza_id} does not exist'}, status=404)
