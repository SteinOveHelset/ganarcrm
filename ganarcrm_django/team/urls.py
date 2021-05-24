from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, UserDetail, get_my_team, add_member, upgrade_plan, get_stripe_pub_key

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/add_member/', add_member, name='add_member'),
    path('teams/upgrade_plan/', upgrade_plan, name='upgrade_plan'),
    path('stripe/get_stripe_pub_key/', get_stripe_pub_key, name='get_stripe_pub_key'),
    path('', include(router.urls)),
]