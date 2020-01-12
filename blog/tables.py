import django_tables2 as tables
from .models import Catalogue


class CatalogueTable(tables.Table):
    date = tables.DateColumn(format='d/m/Y', verbose_name='Date of Register')

    class Meta:
        model = Catalogue
        template_name = 'table.html'
        fields = ('starid', 'name', 'country', 'magnitude', 'constellation', 'date')
        order_by = '-date'
