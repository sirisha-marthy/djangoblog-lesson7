from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through   # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

