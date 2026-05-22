from django.contrib import admin
from .models import Post, category,AboutUs

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=("title","content")
    search_fields=("title","content")
    list_filter=("category","created_at")

admin.site.register(Post,PostAdmin)
admin.site.register(category)
admin.site.register(AboutUs)
