from django.conf.urls import url, include
from rest_framework import routers
from bernini import views_api


router = routers.DefaultRouter()
router.register(r'articulos', views_api.ArticuloViewSet)
urlpatterns = [
    url(r'^', include(router.urls))
]
