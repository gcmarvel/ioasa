from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Article


class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
