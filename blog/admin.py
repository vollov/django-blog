from django.contrib import admin

from blog.models import Blog, Tag

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    #fields = ['posted', 'title']
    list_display = ('title', 'posted', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)