from django.db import models
from sorl.thumbnail import ImageField
from django.utils import timezone

import django_filters


class Article(models.Model):
    title = models.CharField(max_length=500)
    image = ImageField(upload_to='../media/article_images')
    content = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + ' / ' + self.title

    def get_page(self):
        return int(Article.objects.filter(date__gt=self.date).count() / 2 + 1)

    class Meta:
        ordering = ('-date',)


class Catalogue(models.Model):
    starid = models.CharField(max_length=100, verbose_name='Star ID')
    name = models.CharField(max_length=100, verbose_name='Owner')
    country = models.CharField(max_length=100, verbose_name='Country')
    magnitude = models.FloatField(verbose_name='Magnitude')
    constellation = models.CharField(max_length=100, verbose_name='Constellation')
    date = models.DateField()


class CatalogueFilter(django_filters.FilterSet):
    starid = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Catalogue
        fields = ['starid']
