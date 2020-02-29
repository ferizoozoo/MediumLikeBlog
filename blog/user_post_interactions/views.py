from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
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

class IndexPage(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'user/index.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDelete(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('blog:index-user')

class PostUpdate(UpdateView, LoginRequiredMixin):
    model = Post
    context_object_name = 'post'
    template_name = 'user/post.html'
    success_url = reverse_lazy('blog:index-user')
    fields = ['title', 'content']