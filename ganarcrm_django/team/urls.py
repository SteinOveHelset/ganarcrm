from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, get_my_team

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('', include(router.urls)),
]