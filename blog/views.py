from django.shortcuts import render, redirect
from blog.models import blogpostModel, categoryModel
from .forms import blogpostForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    # loading data from database to print it on homepage
    posts = blogpostModel.objects.all()[:11]

    categories = categoryModel.objects.all()
    # print(posts)

    records = {'posts': posts, 'categories': categories}
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
        print('run successs')
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
