from django.contrib import admin
from blog.models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_published',
        'created_at',
        'slug'
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('title', 'description')


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    list_filter = ('category', 'location', 'is_published', 'pub_date')
    search_fields = ('title', 'text')
    list_display_links = ('title',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
