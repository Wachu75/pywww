from django.urls import path
from main.views import hello_world,contact, user_profile

app_name = 'main'

urlpatterns = [
    path('', hello_world, name='base'),
    path('contact', contact, name="contact"),
    path('user/<int:user_id>/profile', user_profile, name="userprofile"),
]