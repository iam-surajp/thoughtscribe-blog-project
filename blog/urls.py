from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, post_detail, categ, create_post, post_edit, post_delete

urlpatterns = [
    path('home/', home, name='home-page'),
    path('blog/<int:pk>', post_detail, name='blog-post-detail'),
    path('category/<int:pk>', categ, name='blog-category-detail'),
    path('create_post/', create_post, name='blog-create-post'),
    path('post_edit/<int:pk>/', post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', post_delete, name='blog-post-delete'),
]
