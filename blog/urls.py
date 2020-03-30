from django.urls import path, include

from .views import * 

app_name = 'blog'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('<int:pk>/', BlogSingleView.as_view(), name='blog_single'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('subscribe/', subscribe, name='subscribe'),
    path('user/', include('blog.user_post_interactions.urls'))
]