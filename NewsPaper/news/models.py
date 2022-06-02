# from accounts.models import Author
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from news.choices import CATEGORIES


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    @staticmethod
    def update_rating(author: "Author") -> None:
        posts_rating = Post.objects.filter(author=author).aggregate(Sum("rating"))["rating__sum"]
        comments_author_rating = Comment.objects.filter(author=author).aggregate(Sum("rating"))["rating__sum"]
        comments_post_rating = Comment.objects.filter(post__author=author).aggregate(Sum("rating"))["rating__sum"]
        author.rating = posts_rating * 3 + comments_author_rating + comments_post_rating
        author.save()

    def __str__(self) -> str:
        return self.user.username


class Category(models.Model):
    category = models.CharField(max_length=256, unique=True)
    subscribers = models.ManyToManyField(User, related_name="categories", blank=True)

    def __str__(self) -> str:
        return self.category


class Post(models.Model):
    text = models.TextField()
    post_type = models.CharField(max_length=16, choices=CATEGORIES)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through="PostCategory")

    def like(self) -> None:
        self.rating += 1
        self.save()

    def dislike(self) -> None:
        self.rating -= 1
        self.save()

    @property
    def preview(self) -> str:
        return self.text[:124] + " ..."

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f"post-{self.pk}")
        print(f"Cache for post-{self.pk} was deleted")


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self) -> None:
        self.rating += 1
        self.save()

    def dislike(self) -> None:
        self.rating -= 1
        self.save()
