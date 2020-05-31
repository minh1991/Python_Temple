from django.contrib import admin
from app_news.models import News

# Register your models here.
# custom show info new
class NewsAdmin(admin.ModelAdmin):
    list_display = ('new_name', 'new_author')
    search_fields = ('new_name','new_author')

admin.site.register(News,NewsAdmin)