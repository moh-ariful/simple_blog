from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'jumlah']
    list_display_links = ['title', 'jumlah']
    search_fields = ['title', 'content']
    list_filter = ['jumlah']  # Membuat filter berdasar jumlah


admin.site.register(Post, PostAdmin)
