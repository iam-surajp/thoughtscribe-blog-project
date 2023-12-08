from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, UserInterestForm
from blog.models import categoryModel, blogpostModel
from .models import interestModel
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


class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)

        # Check if the user has interests selected
        user_has_interests = interestModel.objects.filter(
            user=self.request.user).exists()

        # If the user has interests, redirect them to the home page
        if user_has_interests:
            return redirect('home-page')
        else:
            # If the user doesn't have interests, redirect them to the interests page
            return redirect('user-interests')

    def get(self, request, *args, **kwargs):
        # If the user is already authenticated, redirect them to the home page
        if self.request.user.is_authenticated:
            return redirect('home-page')
        return super().get(request, *args, **kwargs)


@login_required
def profile(request):
    categories = categoryModel.objects.all()
    blogposts = blogpostModel.objects.all()
    interests = interestModel.objects.filter(
        user=request.user).values_list('interests__title', flat=True)

    user = interestModel.objects.get(user=request.user)
    if request.method == 'POST':
        form2 = UserInterestForm(request.POST, instance=user)
        if form2.is_valid():
            # interests = form2.cleaned_data['interests']
            # user.interests.set(interests)
            form2.save()
            return redirect('users-profile')
    else:
        form2 = UserInterestForm(instance=user)

    context = {'categories': categories,
               'posts': blogposts,
               'interests': interests,
               'form2': form2}

    return render(request, 'users/profile.html', context)


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


@login_required
def user_interests(request):
    if request.method == 'POST':
        form = UserInterestForm(
            request.POST)
        if form.is_valid():
            interests = form.cleaned_data['interests']
            user = request.user
            instance, created = interestModel.objects.get_or_create(user=user)
            instance.interests.set(interests)

            return redirect('home-page')
    else:
        form = UserInterestForm()

    return render(request, 'users/interests.html', {'form': form})


def manage_interests(request):
    user = interestModel.objects.get(user=request.user)
    if request.method == 'POST':
        form2 = UserInterestForm(request.POST, instance=user)
        if form2.is_valid():
            # interests = form2.cleaned_data['interests']
            # user.interests.set(interests)
            form2.save()
            return redirect('users-profile')
    else:
        form2 = UserInterestForm(instance=user)
    return render(request, 'users/profile.html', {'form2': form2})
