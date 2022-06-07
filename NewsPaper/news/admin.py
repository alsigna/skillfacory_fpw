from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Author, Category, Comment, Post


def like_post(modeladmin, request, queryset):
    for post in queryset:
        post.like()


def dislike_post(modeladmin, request, queryset):
    for post in queryset:
        post.dislike()


like_post.short_description = "Увеличить рейтинг"
dislike_post.short_description = "Уменьшить рейтинг"


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ("author", "title", "preview")
    list_filter = ("author", "category")
    search_fields = ("text", "title", "category__category", "author__user__username")
    actions = [like_post, dislike_post]


# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)


# Register your models here.

# Регистрируем модели для перевода в админке


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post
