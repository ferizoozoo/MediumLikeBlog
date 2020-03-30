from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):   
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    queryset = Post.objects.all()[::-1]
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel_posts'] = Post.objects.order_by('id')[:3]
        return context

class BlogSingleView(DetailView):
    template_name = 'blog/blog-single.html'
    model = Post
    context_object_name = 'blog_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post'] = Post.objects.latest()
        return context

    def post(self, request, **kwargs):
        if User.is_authenticated:
            comment = Comment(
                post_id = get_object_or_404(Post, pk=self.kwargs['pk']),
                user_id = get_object_or_404(User, pk=request.user.id)
            )
            form = PartialCommentForm(request.POST, instance=comment)
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return HttpResponseRedirect(reverse_lazy('blog:index'))    

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])        