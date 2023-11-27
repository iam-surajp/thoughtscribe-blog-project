from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from blog.models import categoryModel, blogpostModel
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }

    return render(request, 'users/sign_up.html', context)


@login_required
def profile(request):
    categories = categoryModel.objects.all()
    blogposts = blogpostModel.objects.all()
    return render(request, 'users/profile.html', {'categories': categories, 'posts': blogposts})


@login_required
def edit_profile(request):
    categories = categoryModel.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'categories': categories,
    }
    return render(request, 'users/edit_profile.html', context)
