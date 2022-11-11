from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
