from django.urls import path

from .views import * 

app_name = 'blog'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('<int:pk>/', BlogSingleView.as_view(), name='blog_single'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about')
]