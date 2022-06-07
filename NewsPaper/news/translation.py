from .models import Category, Post
from modeltranslation.translator import (
    register,
    TranslationOptions,
)


# регистрируем наши модели для перевода
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("category",)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ("title",)
