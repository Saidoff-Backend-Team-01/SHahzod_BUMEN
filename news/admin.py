from django.contrib import admin

from news.models import News


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['id', 'title']
    search_fields = ['id', 'title']


admin.site.register(News, NewsAdmin)
