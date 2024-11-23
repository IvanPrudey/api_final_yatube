from django.contrib import admin

from .models import Group, Comment, Follow, Post


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = ('text',)
    empty_value_display = 'Не задано'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)
    empty_value_display = 'Не задано'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('following',)
    empty_value_display = 'Не задано'


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
