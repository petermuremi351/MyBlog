from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "title_tag",
            "author",
            "category",
            "body",
            "snippet",
            "header_image",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title of your blog post",
                }
            ),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "peter",
                    "type": "hidden",
                }
            ),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=choice_list, attrs={"class": "form-control"}
            ),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
        }


# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ("title", "title_tag",  "body", "snippet", "header_image")

#     widgets = {
#         "title": forms.TextInput(
#             attrs={"class": "form-control", "placeholder": "Title of your blog post"}
#         ),
#         "title_tag": forms.TextInput(attrs={"class": "form-control"}),
#         # 'author': forms.Select(attrs={'class': 'form-control'}),
#         "body": forms.Textarea(attrs={"class": "form-control"}),
#         "snippet": forms.Textarea(attrs={"class": "form-control"}),
#     }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body", "snippet", "header_image")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title of your blog post",
                }
            ),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,  # taller body field
                }
            ),
            "snippet": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,  # taller snippet field
                    "placeholder": "Write a short snippet...",
                    "style": "resize: vertical;",  # allow vertical resize
                }
            ),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")

    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "body": forms.Textarea(attrs={"class": "form-control"}),
    }
