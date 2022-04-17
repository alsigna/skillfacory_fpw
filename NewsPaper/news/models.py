# from accounts.models import Author
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

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


class Category(models.Model):
    category = models.CharField(max_length=256, unique=True)


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
