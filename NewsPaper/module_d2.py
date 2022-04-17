from news.models import Category, Post, Comment, PostCategory, Author
from django.contrib.auth.models import User


# Создать двух пользователей (с помощью метода User.objects.create_user('username')).
user1 = User.objects.create_user(username="author1", password="password1")
user2 = User.objects.create_user(username="author2", password="password2")


# Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)


# Добавить 4 категории в модель Category.
Category.objects.create(category="sport")
Category.objects.create(category="music")
Category.objects.create(category="medicine")
Category.objects.create(category="astronomy")


# Добавить 2 статьи и 1 новость.
text1 = "Match report as Chelsea overcome Crystal Palace at Wembley to book their place in the FA Cup final, where \
they will face seven-time winners Liverpool on May 14; Ruben Loftus-Cheek and Mason Mount score in second half \
to seal a 2-0 victory for Thomas Tuchel's side"

text2 = "Kanye West doesn’t think The Game should have made recent comments about how he did more for the Compton \
rapper than Dr. Dre, according to Drink Champs host N.O.R.E."

text3 = "As long as there have been people with questions, there have been people looking to the stars for answers. \
While asking the stars for answers might not reveal much, astronomy has been a nearly infinite resource for advances \
in the fields of medicine and medical technology. How has the study of the stars changed our medical technology \
for the better?"

post1 = Post.objects.create(
    text=text1,
    post_type="news",
    title="Chelsea",
    author=author1,
)

post2 = Post.objects.create(
    text=text2,
    post_type="news",
    title="Kanye West",
    author=author1,
)

post3 = Post.objects.create(
    text=text3,
    post_type="article",
    title="Astronomy Influences Advances in Medication & Medical Technology",
    author=author2,
)


# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
PostCategory.objects.create(
    post=post1,
    category=Category.objects.get(category="sport"),
)

PostCategory.objects.create(
    post=post2,
    category=Category.objects.get(category="music"),
)

PostCategory.objects.create(
    post=post3,
    category=Category.objects.get(category="medicine"),
)

PostCategory.objects.create(
    post=post3,
    category=Category.objects.get(category="astronomy"),
)


# Создать как минимум 4 комментария к разным объектам модели Post
# (в каждом объекте должен быть как минимум один комментарий).
comment1 = Comment.objects.create(
    post=post1,
    author=author2,
    text="wow",
)

comment2 = Comment.objects.create(
    post=post2,
    author=author2,
    text="nice",
)

comment3 = Comment.objects.create(
    post=post3,
    author=author1,
    text="cool",
)

comment4 = Comment.objects.create(
    post=post3,
    author=author2,
    text="perfect",
)


# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post1.like()
post2.like()
post3.like()
post3.like()
comment1.like()
comment1.like()
comment2.dislike()
comment2.dislike()
comment2.dislike()
comment3.like()
comment3.like()
comment3.like()
comment4.like()
comment4.like()
comment4.like()


# Обновить рейтинги пользователей.
Author.update_rating(author1)
Author.update_rating(author2)


# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best_author = Author.objects.filter().order_by("-rating").values("user__username", "rating")[0]
print(f"Best author: {best_author['user__username']}\nHis rating: {best_author['rating']}")


# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь
# на лайках/дислайках к этой статье.
best_post = Post.objects.filter().order_by("-rating")[0]
print(
    f"Best post title: {best_post.title}\n"
    f"Create time: {best_post.create_time.strftime('%d-%B-%Y, %H:%M:%S')}\n"
    f"Author name: {best_post.author.user.username}\n"
    f"Rating: {best_post.rating}\n"
    f"Preview: {best_post.preview}\n"
)


# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
for c in best_post.comment_set.all():
    print(
        f"time: {c.create_time.strftime('%d-%B-%Y, %H:%M:%S')}\n"
        f"author: {c.author.user.username}\n"
        f"text: {c.text}\n"
    )
