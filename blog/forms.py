from django import forms
from .models import blogpostModel, Comment


class blogpostForm(forms.ModelForm):

    class Meta:
        model = blogpostModel
        fields = ('title', 'content', 'category', 'pictures')


# class createPostForm(forms.ModelForm):
#     class Meta:
#         model = blogpostModel
#         fields = ['title', 'content', 'category', 'pictures']

    # class Media:
    #     js = (
    #         "https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js", 'js/script.js',)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = blogpostModel
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))

    class Meta:
        model = Comment
        fields = ('content',)
