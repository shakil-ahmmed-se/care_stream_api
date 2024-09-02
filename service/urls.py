from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',views.ServiceViewset, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]
