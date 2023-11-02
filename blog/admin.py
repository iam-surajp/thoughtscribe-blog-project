from django.contrib import admin
from .models import categoryModel, blogpostModel, Comment

# customized category admin


class categoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    search_fields = ('title',)
    list_per_page = 15
    list_filter = ('title',)


class blogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 15

    class Media:
        js = (
            "https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js", 'js/script.js',)


# Register your models here.
admin.site.register(categoryModel, categoryAdmin)
admin.site.register(blogpostModel, blogpostAdmin)
admin.site.register(Comment)
