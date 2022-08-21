from django.contrib import admin

from .models import Post, Group, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "author", "post", "created")
    search_fields = ("text",)
    list_filter = ("created",)
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    search_fields = ("description",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)