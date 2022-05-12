from django import forms
from .models import Post


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = [
            "title",
            "text",
            "author",
            "category",
        ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "post_type",
            "author",
            "category",
        ]
