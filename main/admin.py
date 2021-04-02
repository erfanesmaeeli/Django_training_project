from django.contrib import admin
from main.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'state']
    list_filter = ('state', )
    search_fields = ('title', 'price')
    readonly_fields = ('title', )
    list_editable = ('price', 'state')
    ordering = ('title', '-price')
    sortable_by = ('title', )


admin.site.register(Blog, BlogAdmin)
