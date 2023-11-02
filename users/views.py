from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from blog.models import categoryModel
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

    return render(request, 'users/profile.html', {'categories': categories})
