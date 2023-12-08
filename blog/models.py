from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class categoryModel(models.Model):
    c_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    images = models.ImageField(upload_to="category/")
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.title


class blogpostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = RichTextField(null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    pictures = models.ImageField(null=True, upload_to="post_images/")
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def __str__(self) -> str:
        return self.title

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(blogpostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
