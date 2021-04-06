from django.contrib import admin
from main.models import Blog, Comment, Profile
from django.utils.safestring import mark_safe


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'author', 'price', 'state', 'get_time')
    list_filter = ('state', )
    search_fields = ('title', 'price')
    # readonly_fields = ('title', )
    list_editable = ('price', 'state')
    ordering = ('title', '-price')
    sortable_by = ('title', )
    inlines = (CommentInline, )

    def get_time(self, obj):
        return obj.DateCreated.strftime("%d / %m / %y ساعت %H:%M")

    def get_image(self, obj):
        return mark_safe('<img src="{}" width="80" height="80" loading="lazy"/>'.format("/media/"+str(obj.image)))


    get_time.short_description = 'تاریخ ایجاد'
    get_image.short_description = 'عکس'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog']
    list_filter = ['user']



admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)

