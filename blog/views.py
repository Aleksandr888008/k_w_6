from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog
from django.views import generic


class BlogListView(LoginRequiredMixin, generic.ListView):

    model = Blog
    extra_context = {
        'title': 'Статьи'
    }


class BlogDetailView(LoginRequiredMixin, generic.DetailView):

    model = Blog

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['blog']
        return context_data

    def get_object(self, queryset=None):

        item = super().get_object(queryset)
        item.count_views += 1   # считаем просмотры
        item.save()
        return item
