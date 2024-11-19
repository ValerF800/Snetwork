from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from articles.models import Articles


class ArticlesView(ListView):
    model = Articles
    template_name = 'articles/articles.html'
    context_object_name = 'posts'


class ArticlesSubView(ListView):
    model = Articles
    template_name = 'articles/articles.html'
    context_object_name = 'posts'

    def get_queryset(self):
        authors = self.request.user.following.values_list('id', flat=True)
        queryset = self.model.objects.all().filter(author__id__in=authors)
        return queryset


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Статьи авторов'
    #     return context


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'articles/article.html'
    context_object_name = 'post'


class ArticlesCreateView(CreateView):
    model = Articles
    template_name = 'articles/article-create.html'
    fields = ['title', 'description', 'author']

class ArticlesUpdateView(UpdateView):
    model = Articles
    template_name = 'articles/article-update.html'
    fields = ['title', 'description', ]

    def get_success_url(self):
        article_id = self.kwargs['pk']
        return reverse_lazy('article', kwargs={'pk': article_id})

