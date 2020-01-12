from django.urls import path

from .views import MainView, CatalogueView, PartnersView, AboutView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('partners/', PartnersView.as_view(), name='partners'),
    path('about/', AboutView.as_view(), name='about')
]
