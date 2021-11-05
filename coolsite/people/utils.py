from .models import *


menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add post', 'url_name': 'add_post'},
        {'title': 'Feedback', 'url_name': 'feedback'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
