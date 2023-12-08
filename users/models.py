from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from blog.models import categoryModel
# Create your models here.


class profileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile',
                              validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])

    def __str__(self) -> str:
        return self.user.username


class interestModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(categoryModel, blank=True)
