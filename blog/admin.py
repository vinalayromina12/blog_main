#--*--ciding:-utf-8--*-


from django.contrib import admin
from .models import Category, Comment, Post


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ('title', 'category', 'created_at', 'status')
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ('title', 'category', 'created at', 'status')
    list_filter = ['category', 'created at', 'status']
    inlines = [CommentItemInline]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
