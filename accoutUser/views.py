from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import UserRegForm, UserUpdateForm, UserUpdateProfileForm
from .models import UserProfileModel
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login


def user_reg(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Профиль пользователя {username} успешно создан')
            return redirect('home')
    else:
        form = UserRegForm()
    context = {'form': form}
    return render(request, 'accoutUser/registration.html', context)


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'accoutUser/login.html'

    def get_success_message(self, cleaned_data):
        username = cleaned_data['username']
        return f'Добро пожаловать, {username}!'


class UserProfileView(DetailView):
    context_object_name = 'profile'
    template_name = 'accoutUser/profile.html'

    def get_queryset(self):
        return UserProfileModel.objects.filter(pk=self.kwargs['pk'])


@login_required
def update_user_profile(request):
    if request.method == 'POST':
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = UserUpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofilemodel)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, f'Профиль пользователя {request.user} успешно отредактирован')
            return redirect('profile', pk=request.user.userprofilemodel.pk)
    else:
        form1 = UserUpdateForm(instance=request.user)
        form2 = UserUpdateProfileForm(instance=request.user.userprofilemodel)
    context = {
        'form1': form1,
        'form2': form2
        }
    return render(request, template_name='accoutUser/profile_update.html', context=context)
