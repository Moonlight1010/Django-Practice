from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_created')
    list_display_links = ('title',)
    list_filter = ('title', 'user', 'date_created')
    search_fields = ('title', 'date_created')