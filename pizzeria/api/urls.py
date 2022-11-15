from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, PostApiView, PizzaApiView, CategoryApiView, ProductApiView


router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/posts/', PostApiView.as_view(), name='api-posts'),
    path('api/posts/<int:post_id>', PostApiView.as_view(), name='api-post'),
    path('api/pizza/', PizzaApiView.as_view(), name='api-pizzas'),
    path('api/pizza/<int:pizza_id>', PizzaApiView.as_view(), name='api-pizza'),
    path('api/category/', CategoryApiView.as_view(), name='api-categories'),
    path('api/category/<int:category_id>', CategoryApiView.as_view(), name='api-category'),
    path('api/category/<int:category_id>/product/', ProductApiView.as_view(), name='api-products'),
    path('api/category/<int:category_id>/product/<int:product_id>', ProductApiView.as_view(), name='api-product'),


]
