from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models
import readtime
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author','publish', 'status', 'reading_time', 'article_image']
    list_filter = ['status','created', 'publish','author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    def save_model(self, request, obj, form, change):
        obj.reading_time = readtime.of_html(obj.body)

        super().save_model(request, obj, form, change)