from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import UserSignupForm
from users.mixins import ProfileAccessMixin
from users.models import User


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'
    ''''por padrão, o context_object_name é o nome do model (antes de definir
    que era 'profile', estava 'user')'''


class ProfileEditView(ProfileAccessMixin, UpdateView):
    model = User
    fields = ('picture', 'username', )
    template_name = 'profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.pk])


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('tuites:post') 


#UpdateView é a view usada para editar um objeto
