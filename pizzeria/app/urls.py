from django.urls import path, register_converter, re_path
from .views import IndexView, AboutView, ContactView, ServicesView, BlogView, PostView, MenuView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('<slug:post_slug>/', PostView.as_view(), name='post'),
]
