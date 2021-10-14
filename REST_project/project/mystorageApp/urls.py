from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('albums', views.ImageViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
