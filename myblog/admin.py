from django.contrib import admin
from myblog.models import Post, Category
from django.core.urlresolvers import reverse


class ModelAdmin(admin.ModelAdmin):
    """both post andd category"""
    def get_urls(self):
        urls = super(MyModelAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^my_view/$', 
self.admin_site.admin_view(self.my_view, cacheable=True))
        )
        return my_urls + urls

class PostAdmin(admin.ModelAdmin):
    """supress display of link"""
    list_display = ('__unicode__', 'created_date', 'modified_date',
                    'published_date', 'author_link')

admin.site.register(Post, PostAdmin)

class CategoryInlineAdmin(admin.ModelAdmin):
	"""edit categorys on Posts"""
        model = Category.posts.through
        extra = 1



admin.site.register(Post)
admin.site.register(Category) 