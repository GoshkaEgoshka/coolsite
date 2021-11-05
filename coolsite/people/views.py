from django.http import HttpResponse
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import AddPostForm, RegisterUserForm
from .utils import DataMixin, menu

from .models import *


class PeopleHome(DataMixin, ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(contex.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('Page not found :(')

def about(request):
    return render(request, 'people/about.html', {'menu': menu,'title': 'About'})

class AddPost(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'people/add_post.html'

    def get_context_data(self, *, object_list=None ,**kwargs):
        contex = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add post")
        return dict(list(contex.items()) + list(c_def.items()))

def feedback(request):
    return HttpResponse('Feedback')

def login(request):
    return HttpResponse('Login page')

class PeopleCategory(DataMixin, ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return People.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                    cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'people/post.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'people/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))
