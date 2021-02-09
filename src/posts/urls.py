from django.urls import path

from .views import posts_comment_create_list_view , like_unlike_post

app_name ='posts'

urlpatterns = [
    path('post/' , posts_comment_create_list_view , name= 'main-post-view'),
    path('liked/' , like_unlike_post , name= 'liked_post_view'),

]