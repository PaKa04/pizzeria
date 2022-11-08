from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Pizza, Category, Product, Cart, Post
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
    posts = Post.objects.all().order_by('date_published')
    context = {
        'posts': posts
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        context = self.context
        return render(request, self.template_name, context)


class PostView(BlogView, DetailView):
    template_name = 'app/blog-single.html'

    def get(self, request, post_slug):
        post = get_object_or_404(Post, slug=post_slug)
        context = self.context
        context['post'] = post
        return render(request, self.template_name, context)


def error404(request, exception):
    return HttpResponse('404 not found')
