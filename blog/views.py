from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from .models import *
from .forms import *

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
        context['last_post'] = Post.objects.latest()
        return context

    # TODO: Comment posting needs to be corrected.
    def post(self, request, **kwargs):
        if User.is_authenticated:
            comment = Comment(
                post_id = get_object_or_404(Post, pk=self.kwargs['pk']),
                user_id = get_object_or_404(User, pk=request.user.id)
            )
            form = PartialCommentForm(request.POST, instance=comment)
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return HttpResponseRedirect(reverse('login'))    

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class SubscribeView(CreateView):
    pass