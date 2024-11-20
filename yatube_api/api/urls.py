from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_ver_1 = routers.DefaultRouter()
router_ver_1.register('groups', GroupViewSet, basename='group')
router_ver_1.register('posts', PostViewSet, basename='post')
router_ver_1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_ver_1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_ver_1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
