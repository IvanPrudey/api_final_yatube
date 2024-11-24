from django.contrib import admin

from posts.models import Group, Comment, Follow, Post


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description',)
    empty_value_display = 'Не задано'
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group',)
    empty_value_display = 'Не задано'
    search_fields = ('text', 'author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author', 'created')
    empty_value_display = 'Не задано'
    search_fields = ('text', 'author',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following',)
    empty_value_display = 'Не задано'
    search_fields = ('user', 'following',)
