from django.contrib import admin

# Register your models here.


from django.contrib import admin


from django.contrib.admin import ModelAdmin

from .models import Blog
class BlogAdmin(ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)

from django.contrib import admin


from django.contrib.admin import ModelAdmin

from .models import Comment
class CommentAdmin(ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)