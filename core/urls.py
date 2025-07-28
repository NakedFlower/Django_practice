from django.urls import path, include
from .views import PlaceList
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('places_old/', PlaceList.as_view()),
    path('', include(router.urls)),
]
