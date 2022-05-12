from cgitb import text
import os
from datetime import datetime
from turtle import title

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
django.setup()

import random
from news.models import Category, Post, Comment, PostCategory, Author


class Data:
    def __init__(
        self,
        author: Author,
        post_type: str,
        category: Category,
        title: str,
        text: str,
    ) -> None:
        self.author = author
        self.post_type = post_type
        self.category = category
        self.title = title
        self.text = text


authors = [
    Author.objects.get(user__username="author1"),
    Author.objects.get(user__username="author2"),
]

post_types = ["news", "article"]

sport = Category.objects.get(category="sport")
music = Category.objects.get(category="music")
medicine = Category.objects.get(category="medicine")
astronomy = Category.objects.get(category="astronomy")

data = [
    Data(
        random.choice(authors),
        random.choice(post_types),
        astronomy,
        "101 Must-See Cosmic Objects: Omega Centauri",
        "The most glorious of all globular clusters is Omega Centauri. (NGC 5139 is its more mundane designation.) \
It’s the 24th-brightest “star” in Centaurus, which is the ninth largest of 88 constellations. It was noted in \
Ptolemy’s Almagest in A.D. 150 and designated Omega (ω) by Johann Bayer in his 1603 Uranometria. Edmond Halley \
is credited for first noting its non-stellar appearance in 1677. Scottish astronomer James Dunlop first described \
it as a globular cluster in 1826.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        astronomy,
        "Can we protect Earth from an asteroid speeding toward us?",
        "The most famous asteroid to collide with Earth is the Chicxulub crater, which hit the Yucatán Peninsula \
65 million years ago. It’s known for wiping out the dinosaurs, along with three quarters of life on the planet. \
Other huge craters like the Vredefort crater in South Africa and the Sudbury Basin in Ontario, Canada were even \
larger and likely barreled toward us a couple billion years ago.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        astronomy,
        "The northern lights: A history of aurora sightings",
        "Throughout history, humans have gazed in awe at the astronomical wonder that is the aurora borealis. \
We’ve wondered what it is and told stories about the lights that shimmered above.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        music,
        "Glastonbury 2022 confirms line-up for the Acoustic Stage",
        "This latest addition to the growing Worthy Farm bill for this year’s festival, which is held from \
June 22-26, follows on from recent line-up announcements for the Glade, Common, Left Field and Shangri-La areas.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        music,
        "Young Thug has been charged with seven additional felonies",
        "After being arrested for alleged gang-related activity earlier this week, \
Young Thug has now been charged with seven more felonies.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        sport,
        "Mercedes explain Miami GP strategy after Lewis Hamilton confusion: 'Between rock and a hard place'",
        "Mercedes explain their strategy calls - and asking Lewis Hamilton for his input - at the Miami GP after \
George Russelll capitalised on the Safety Car to pass his team-mate, finishing ahead for the fourth race in a row",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        sport,
        "Celtic win the Scottish Premiership",
        "Celtic are the Scottish Premiership champions again in what has been a memorable \
debut season for manager Ange Postecoglou.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        sport,
        "Greg Norman says ‘we all make mistakes’ when asked about Khashoggi killing",
        "The golf champion Greg Norman has attempted to dismiss questions over the murder of the journalist \
Jamal Khashoggi at a Saudi consulate as a “mistake,” adding the Saudi government “wants to move forward”.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        medicine,
        "Lawsuit Against Cedars-Sinai Alleges Racial Discrimination in Treatment of Black Mother",
        "The widower of a Black woman who died hours after a cesarean delivery has filed a civil rights \
lawsuit against Cedars-Sinai Medical Center in Los Angeles, alleging that his wife received inferior care \
because of the color of her skin.",
    ),
    Data(
        random.choice(authors),
        random.choice(post_types),
        medicine,
        "Another Ivermectin-COVID-19 Paper Is Retracted",
        "A paper on the potential use of ivermectin to treat Covid-19 has been retracted for a litany of \
flaws, joining at least 10 other articles on the therapy some liked to promote without evidence to fall.",
    ),
]

for to_add in data:
    post = Post.objects.create(
        author=to_add.author,
        post_type=to_add.post_type,
        title=to_add.title,
        text=to_add.text,
    )
    PostCategory.objects.create(
        post=post,
        category=to_add.category,
    )


for author in authors:
    Author.update_rating(author)
