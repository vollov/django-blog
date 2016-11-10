from django.contrib import admin

from blog.models import Blog, Tag, BlogTag, Course

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    #fields = ['posted', 'title']
    list_display = ('title', 'created_at', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)

class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['blog','tag', 'created_at']
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['tag','created_at']
    
    list_filter = ['tag','created_at']
    
admin.site.register(BlogTag, BlogTagAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']

admin.site.register(Course, CourseAdmin)