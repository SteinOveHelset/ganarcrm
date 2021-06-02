from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, UserDetail, get_my_team, cancel_plan, add_member, upgrade_plan, get_stripe_pub_key, check_session, create_checkout_session, stripe_webhook

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/add_member/', add_member, name='add_member'),
    path('teams/upgrade_plan/', upgrade_plan, name='upgrade_plan'),
    path('teams/cancel_plan/', cancel_plan, name='cancel_plan'),
    path('stripe/get_stripe_pub_key/', get_stripe_pub_key, name='get_stripe_pub_key'),
    path('stripe/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook/', stripe_webhook, name='stripe_webhook'),
    path('stripe/check_session/', check_session, name='check_session'),
    path('', include(router.urls)),
]