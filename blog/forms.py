from django import forms

from .models import Comment, Post
from django.db import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        post = Post.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'