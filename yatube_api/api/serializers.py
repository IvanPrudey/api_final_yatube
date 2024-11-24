from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User

MESSAGE_DONE = 'Уже подписаны на этого автора.'
MESSAGE_YOURSELF = 'Вы не можете подписаться на себя.'


class GroupSerializer(serializers.ModelSerializer):
    '''Сериализатор к модели Group.'''

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    '''Сериализатор к модели Post.'''

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    '''Сериализатор к модели Comment.'''

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post']


class FollowSerializer(serializers.ModelSerializer):
    '''Сериализатор к модели Follow.'''

    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    # по вашему комментарию - добавляю имя поля validate_following, сразу
    # не проходит 1 тест. если оставляю просто validate то все тесты проходят
    # что делаю не так?
    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        is_unique = Follow.objects.filter(
            user=user, following=following
        ).exists()
        if user == following:
            raise serializers.ValidationError(f'{MESSAGE_YOURSELF}')
        if is_unique:
            raise serializers.ValidationError(f'{MESSAGE_DONE}')
        return data
