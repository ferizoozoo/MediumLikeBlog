from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import UserCreationForm, UserProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpRequest

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileUpdateForm
    context_object_name = 'owner'
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile', kwargs = {'pk': self.kwargs['pk']})