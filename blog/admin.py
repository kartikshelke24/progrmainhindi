from django.contrib import admin
from blog.models import BlogComment, BlogPost


# Register your models here.
admin.site.register(BlogComment)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyMCEinject.js',)
