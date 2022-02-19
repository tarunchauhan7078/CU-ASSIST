from django.contrib import admin

# Register your models here.
from .models import Post, postComment

admin.site.register((postComment))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinyInject.js')