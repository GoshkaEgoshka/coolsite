from django.urls import path

from .views import *

urlpatterns = [
    path('', PeopleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>', show_post, name='post'),
    path('category/<slug:cat_slug>', PeopleCategory.as_view(), name='category'),
]
