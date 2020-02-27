from django.urls import path
from .views import *

app_name = 'user_post_interactions'
urlpatterns = [
    path('post/', PostCreate.as_view(), name='post'),
    path('delete/', PostDelete.as_view(), name='delete'),
    path('update/', PostUpdate.as_view(), name='update')
]