from django.contrib import admin

from posts.models import Group, Comment, Follow, Post


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description',)
    empty_value_display = 'Не задано'
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group',)
    empty_value_display = 'Не задано'
    search_fields = ('text', 'author',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author', 'created')
    empty_value_display = 'Не задано'
    search_fields = ('text', 'author',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following',)
    empty_value_display = 'Не задано'
    search_fields = ('user', 'following',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
