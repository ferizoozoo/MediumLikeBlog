from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import *

# Views for the user interactions with the posts.
class PostCreate(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'user/post.html'
    success_url = '/blog'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class PostDelete(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = ''

class PostUpdate(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = ''