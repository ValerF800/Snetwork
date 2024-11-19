from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import View

from Snetwork.settings import DEFAULT_USER_IMAGE, MEDIA_URL
from profiles.forms import LoginUserForm, ProfileForm, RegisterUserForm, CreateMessageForm
from profiles.models import Message, User


def Testview(request):
    return render(request, 'base/index.html')

def Registerview(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('profile', user.id)

    return render(request, 'profile/register.html', {'form': form})

def Loginview(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('profile', user.id)

    return render(request, 'base/login.html')

def Logoutview(request):
    logout(request)
    return render(request, 'base/logout.html')

def Profiles(request):
    model = get_user_model()
    profiles = model.objects.all()
    return render(request, 'profile/profiles.html', {'profiles': profiles})

def ProfileDetail(request, pk):
    model = get_user_model()
    profile = model.objects.get(pk=pk)

    extra_content = {'profile': profile,
        'default_image' : DEFAULT_USER_IMAGE}

    return render(request, 'profile/profile-detail.html', context=extra_content)

def ProfileChange(request, pk):
    model = get_user_model()
    profile = model.objects.get(pk=pk)

    if request.user == profile or request.user.is_superuser:
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            # model = get_user_model()
            # profile = model.objects.get(pk=pk)
            # profile.photo = request.FILES['image']
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile', pk)

        return render(request, 'profile/change-profile.html', context={'form' : form})
    else:
        return HttpResponseForbidden()


def CreateMessage(request):
    form = CreateMessageForm()
    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()

        return redirect('profiles')
            # return render(request, 'profile/profiles.html')
    return render(request, 'profile/create-message.html', {'form': form})


def inbox(request):
    messages = User.objects.get(pk=request.user.id).messages.all()
    return render(request, 'profile/inbox.html', {'messages': messages})



# @method_decorator(login_required, name='dispatch')
class ProfileFollowingCreateView(View):
    """
    Создание подписки для пользователей
    """
    model = User

    def is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def post(self, request, pk):
        user = self.model.objects.get(id=pk)
        profile = request.user
        if profile in user.followers.all():
            user.followers.remove(profile)
            message = f'Подписаться на {user}'
            status = False
        else:
            user.followers.add(profile)
            message = f'Отписаться от {user}'
            status = True
        data = {
            'username': profile.username,
            # 'get_absolute_url': profile.get_absolute_url(),
            # 'slug': profile.slug,
            # 'avatar': profile.get_avatar,
            'message': message,
            'status': status,
        }
        return JsonResponse(data, status=200)











