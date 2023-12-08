from django.shortcuts import render, redirect
from blog.models import blogpostModel, categoryModel
from .forms import blogpostForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from users.models import interestModel
from random import shuffle
# Create your views here.


@login_required
def home(request):
    # Get the user's interests
    user_interests = []
    if request.user.is_authenticated:
        # Step 1: Retrieve user's interests
        user_interests = interestModel.objects.filter(
            user=request.user).values_list('interests__title', flat=True)

    # Step 2: Retrieve associated category IDs
    category_ids = interestModel.objects.filter(
        user=request.user
    ).values_list('interests__title', flat=True)

    # Step 3: Filter blog posts based on user interests
    if user_interests is not None and user_interests:  # Check if user_interests is not an empty list
        posts_in_interests = blogpostModel.objects.filter(
            category__title__in=user_interests
        )
        # Shuffle the list of posts_in_interests
        shuffled_posts_in_interests = list(posts_in_interests)
        shuffle(shuffled_posts_in_interests)
    elif not user_interests:
        shuffled_posts_in_interests = list(blogpostModel.objects.all())
        print("User has no selected interests. All posts will be displayed.")

    # Get other posts
    other_posts = blogpostModel.objects.exclude(
        category__title__in=user_interests
    )

    # Combine posts in interests and other posts
    all_posts = shuffled_posts_in_interests + list(other_posts)

    paginator = Paginator(all_posts, 7)
    page_number = request.GET.get('page')
    final_posts = paginator.get_page(page_number)
    total_pages = final_posts.paginator.num_pages

    categories = categoryModel.objects.all()

    records = {'posts': all_posts, 'categories': categories,
               'final_posts': final_posts, 'total_pagelist': [n+1 for n in range(total_pages)]}
    return render(request, "blog/home.html", records)


@login_required
def post_detail(request, pk):
    post = blogpostModel.objects.get(id=pk)
    categories = categoryModel.objects.all()
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
        'categories': categories,
    }

    return render(request, "blog/post_detail.html", context)


@login_required
def categ(request, pk):
    cat = categoryModel.objects.get(c_id=pk)
    posts = blogpostModel.objects.filter(category=cat)
    categories = categoryModel.objects.all()
    return render(request, 'blog/category.html', {'cat': cat, 'posts': posts, 'categories': categories})


@login_required
def create_post(request):
    categories = categoryModel.objects.all()
    if request.method == "POST":
        form = blogpostForm(request.POST, request.FILES)
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        category = categoryModel.objects.get(c_id=category_id)
        pictures = request.FILES.get('pictures')
        author = request.user
        blogpostModel.objects.create(
            title=title, content=content, author=author, category=category, pictures=pictures)
        # messages.success(request,'Data has been submitted')
        # instance.author = request.user
        # instance.save()
        return redirect('home-page')
    else:
        form = blogpostForm()
    return render(request, 'blog/create_post.html', {'form': form, 'categories': categories, })


@login_required
def post_edit(request, pk):
    post = blogpostModel.objects.get(id=pk)
    categories = categoryModel.objects.all()
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
        'categories': categories,
    }
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_delete(request, pk):
    post = blogpostModel.objects.get(id=pk)
    categories = categoryModel.objects.all()
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'blog/post_delete.html', context)
