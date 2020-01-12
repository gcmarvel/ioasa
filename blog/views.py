from django.views.generic import ListView, TemplateView
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import Article, Catalogue, CatalogueFilter
from .tables import CatalogueTable
from .tabledata import new_data
import datetime
import random


class MainView(ListView):
    template_name = 'main.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        small_articles = Article.objects.all()[:5]
        try:
            medium_articles = random.sample(list(Article.objects.filter(date__lte=datetime.datetime.now(), date__gt=datetime.datetime.now() - datetime.timedelta(days=356))), 3)
        except ValueError:
            medium_articles = Article.objects.filter(date__lte=datetime.datetime.now(), date__gt=datetime.datetime.now() - datetime.timedelta(days=356))
        context['small_articles'] = small_articles
        context['medium_articles'] = medium_articles
        return context


class CatalogueView(SingleTableMixin, FilterView):
    template_name = 'catalogue.html'
    model = Catalogue
    table_class = CatalogueTable
    table_data = new_data

    filterset_class = CatalogueFilter

    table_pagination = {
        'per_page': 20
    }

    def get_queryset(self):
        qs = self.request.GET.get('starid')
        data_list = new_data

        def generate_data(qs, data_list):
            global newest_data
            newest_data = [x for x in data_list if x['starid'] == str(qs)]
            return newest_data

        generate_data(qs, data_list)

    def get_table_data(self):
        if newest_data == []:
            return new_data
        else:
            return newest_data


class PartnersView(TemplateView):
    template_name = 'partners.html'


class AboutView(TemplateView):
    template_name = 'about.html'
