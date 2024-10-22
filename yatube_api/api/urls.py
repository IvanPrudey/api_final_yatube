from django.urls import include, path
from rest_framework import routers

from .views import CommentViewset, GroupViewset, PostViewset


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
# router.register('follow', FollowViewset, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    # path('v1/api-token-auth/', views.obtain_auth_token),
]
