from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views import View


from .forms import SignUpForm, SignInForm
from app.models import Cart
from app.views import IndexView


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('signin')


class SignInView(LoginView):
    template_name = 'registration/signin.html'
    form_class = SignInForm


class CartView(LoginRequiredMixin, IndexView):
    template_name = 'registration/cart.html'
    login_url = '/signin/'

    def get(self, request: HttpRequest) -> HttpResponse:
        user = User.objects.filter(username=request.user)[0]
        user_products = Cart.objects.filter(user=request.user.id)
        content = self.get_context_data()
        content['user'] = user
        content['user_products'] = user_products
        prices = []
        for i in user_products:
            for p in content['products']:
                if i.name == p.title:
                    prices.append(p.price)
            for pi in content['pizzas']:
                if i.name == pi.name:
                    prices.append(pi.price)

        total_price = sum(prices)
        content['total_price'] = total_price
        content['count_userproducts'] = len(user_products)
        return render(request, self.template_name, content)

