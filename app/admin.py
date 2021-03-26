from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_swiper', 'create_date')

    '''filter options'''
    list_filter = ('is_swiper', )

    '''10 items per page'''
    list_per_page = 10

admin.site.register(Article, ArticleAdmin)