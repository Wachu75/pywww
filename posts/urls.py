from django.urls import path
from posts.views import posts_list, post_details, add_post, add_post_form, edit_post, save_post

app_name = 'posts'

urlpatterns = [
    path('', posts_list, name='list'),
    path("<int:post_id>", post_details, name='details'),
    path('add', add_post_form, name="add"),
    path('edit/<int:post_id>', edit_post, name="edit"),
    path('save', save_post, name="save"),
]