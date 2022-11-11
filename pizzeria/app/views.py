from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils.timezone import now

from .models import Pizza, Category, Product, Cart, Post, Comments
from django.views import View
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class IndexView(View):
    template_name = 'app/index.html'

    def get_context_data(self):
        pizzas = Pizza.objects.all()
        ing_piz = {}
        for pizza in pizzas:
            ing = []
            ingr = pizza.ingridients.all().values().order_by('name')
            for el in list(ingr):
                pizza_ingridients = el['name']
                ing.append(pizza_ingridients)
            ing_piz[pizza.name] = ", ".join(ing)
        two_column_pizzas = zip(pizzas[::2], pizzas[1::2])

        categories = Category.objects.all().order_by('name')
        products = Product.objects.filter(is_published=1).order_by('title')
        content = {
            'categories': categories,
            'products': products,
            'ing': ing_piz,
            'pizzas': pizzas,
            'columns_pizza': two_column_pizzas,
            'contact_form': ContactForm(),
            'contact_error': None,
            'posts': Post.objects.all().order_by('date_published')[0:5]
        }
        return content

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        if request.POST['action'] == 'Send':
            form = ContactForm(request.POST)
            content = self.get_context_data()
            if form.is_valid():
                form.save()
            else:
                content['contact_error'] = "Error"
            return render(request, self.template_name, content)

        elif request.POST['action'] == 'Add to Cart':
            b = Cart()
            b.user_id = request.POST['User']
            b.name = request.POST['Nameofprod']

            b.save()
            content = self.get_context_data()
            return render(request, self.template_name, content)

        elif request.POST['action'] == 'Clear CART':
            user = request.POST['User']
            c = Cart.objects.filter(user_id=user)
            c.delete()
            content = self.get_context_data()
            return render(request, self.template_name, content)


class AboutView(IndexView):
    template_name = 'app/about.html'


class ContactView(IndexView):
    template_name = 'app/contact.html'


class MenuView(IndexView):
    template_name = 'app/menu.html'


class ServicesView(IndexView):
    template_name = 'app/services.html'


class BlogView(View):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog.html'
    posts = Post.objects.all().filter(is_published=True).order_by('date_published')
    context = {
        'posts': posts
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        context = self.context
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.context
        posts = Post.objects.all().order_by('date_published')
        search_request = request.POST
        search_posts = []
        for post in posts:
            if f'{search_request["search"]}'.lower() in f'{post.title}'.lower():
                search_posts.append(post)
        context['posts'] = search_posts
        return render(request, self.template_name, context)


class PostView(BlogView, DetailView):
    template_name = 'app/blog-single.html'
    slug_url_kwarg = 'post_slug'

    def get(self, request, **kwargs):
        posts = Post.objects.all().filter(is_published=True).order_by('date_published')[0:5]
        post = get_object_or_404(Post, slug=kwargs['post_slug'])
        comments = Comments.objects.filter(post_id=post.id)
        context = self.context
        context['post'] = post
        context['posts'] = posts
        context['comments'] = comments
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        print(request.POST)
        if request.POST['action'] == 'Post Comment':
            context = self.context
            b = Comments()
            b.user = request.POST['User']
            b.post_id = request.POST['SUPOST']
            b.text = request.POST['FUCK']
            b.date_published = now()
            b.save()
        elif request.POST['action'] == 'Delete Comment':
            c = Comments.objects.filter(id=request.POST['CommentID'])
            c.delete()
            context = self.context
            comments = Comments.objects.filter(post_id=request.POST['PostID'])
            context['comments'] = comments
        return render(request, self.template_name, context)


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
