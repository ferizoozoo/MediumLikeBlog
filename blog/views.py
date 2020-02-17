from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .views import *
from .models import *

# Create your views here.
class IndexView(ListView):
    
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    queryset = Post.objects.all()[::-1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ## TODO: get context for carousel posts but definitely needs to be changed!
        context['carousel_posts'] = Post.objects.all()
        return context

class BlogSingleView(DetailView):
    template_name = 'blog/blog-single.html'
    model = Post
    context_object_name = 'blog_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(pk = self.kwargs['pk'])
        return context

class ContactView(TemplateView):
    pass

class AboutView(TemplateView):
    pass