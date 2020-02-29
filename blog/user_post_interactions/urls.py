from django.urls import path
from .views import *

urlpatterns = [
    path('post/', PostCreate.as_view(), name='post'),
    path('index/', IndexPage.as_view(), name='index-user'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update')
]