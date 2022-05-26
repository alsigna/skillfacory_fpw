from django import forms
from django.contrib.auth.models import User

from .models import Category, Post


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


class SubscriptionEditForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categories"].initial = self.instance.categories.all().values_list("id", flat=True)

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        instance.categories.set(self.cleaned_data["categories"])
        return instance

    class Meta:
        model = User
        fields = [
            "categories",
        ]
