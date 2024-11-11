from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


from .permissions import IsAuthorOrReadOnlyPermission
from posts.models import Group, Post
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    """Документация от себя."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnlyPermission,)
    # pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnlyPermission,)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments.all()


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
