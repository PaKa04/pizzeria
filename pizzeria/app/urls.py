from django.urls import path, register_converter, re_path
from .views import IndexView, AboutView, ContactView, ServicesView, BlogView, PostView, MenuView, PostApiView, CategoryApiView, ProductApiView, PizzaApiView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('api/posts/', PostApiView.as_view(), name='api-posts'),
    path('api/posts/<int:post_id>', PostApiView.as_view(), name='api-post'),
    path('api/pizza/', PizzaApiView.as_view(), name='api-pizzas'),
    path('api/pizza/<int:pizza_id>', PizzaApiView.as_view(), name='api-pizza'),
    path('api/category/', CategoryApiView.as_view(), name='api-categories'),
    path('api/category/<int:category_id>', CategoryApiView.as_view(), name='api-category'),
    path('api/category/<int:category_id>/product/', ProductApiView.as_view(), name='api-products'),
    path('api/category/<int:category_id>/product/<int:product_id>', ProductApiView.as_view(), name='api-product'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('blog/<slug:post_slug>/', PostView.as_view(), name='post'),
]
