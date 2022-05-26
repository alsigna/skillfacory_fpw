from turtle import title
from django import forms
from django_filters import FilterSet, ModelChoiceFilter, DateFilter, ChoiceFilter
from .models import Post, Author, Category
from .choices import CATEGORIES


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        label="Author",
        empty_label="Any",
    )
    start = DateFilter(
        field_name="create_time",
        widget=forms.DateInput(attrs={"type": "date"}),
        lookup_expr="gt",
        label="Published after",
    )
    post_type = ChoiceFilter(
        choices=CATEGORIES,
        label="Post Type",
        empty_label="Any",
    )
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="Category",
        empty_label="Any",
    )

    class Meta:
        model = Post
        fields = {
            "title": ["icontains"],
        }
