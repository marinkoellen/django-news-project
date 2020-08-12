from django.contrib import admin
from .models import NewsStory
# Register your models here.

@admin.register(NewsStory)
class NewsStoryAdmin(admin.ModelAdmin):
    pass