from django.contrib import admin
from .models import Post, Tag, Author
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags","date",)
    list_display=("title","date","author",)
prepopulated_fields={"alug":("title")}
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
