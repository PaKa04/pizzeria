from django.urls import path
from .views import SignInView, SignUpView, CartView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/cart/', CartView.as_view(), name='cart'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
