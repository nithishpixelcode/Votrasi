from django.utils.safestring import mark_safe
from django.contrib import admin
from gallery.models import *
from sorl.thumbnail import *
from django.utils.safestring import mark_safe

ADMIN_THUMBS_SIZE = '60x60'

def add(list_, short_description=None, position=None, **kwargs):
    """
    A helper to add a method to `list_` (usually `ModelAdmin.list_display`),
    where the method's name is added, and items may have attributes like
    `short_description` and `boolean`.
    
    `position` is the index at which to insert the item. By default, items
    are appended.
    
    Example:
    
    class ExampleAdmin(admin.ModelAdmin):
        list_display = ['__str__']
        
        @add(list_display, "in progress?", boolean=True)
        def in_progress(self, object):
            return not object.is_complete
    
        @add(list_display, mark_safe('&#x2713;'), 0, allow_tags=True)
        def checkbox(self, object):
            return '<input type="checkbox" value="%s"/>' % object.pk
    
    """
    if short_description is not None:
        kwargs['short_description'] = short_description
    def decorate(f):
        if isinstance(f, basestring):
            list_.append(f)
        else:
            for key, value in kwargs.iteritems():
                setattr(f, key, value)
            if position is None:
                list_.append(f.__name__)
            else:
                list_.insert(position, f.__name__)
            return f
    return decorate

class CategoryImageAdmin(admin.ModelAdmin):
	
	prepopulated_fields={'slug':('title',)}
	list_display = ['order','title', 'image_category', 'date_created' ,'is_publish'] #,'my_image_thumb')
        list_filter = ('image_category', 'is_publish')

	@add(list_display, 'Image', 0, allow_tags=True)
	def image_(self, obj):
	    return mark_safe('<img width="200" src="'+obj.image.url+'" />')
	
"""	
	def my_image_thumb(self, obj):
		if obj.image(self, obj):
		    thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
		    return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
		else:
		    return "No Image" 
	my_image_thumb.short_description = 'Image Thumbnail'
	my_image_thumb.allow_tags = True
"""
class CategoryAdmin(admin.ModelAdmin):
	
	prepopulated_fields={'slug':('title',)}
	list_display = ('category_name', 'date_created') ##,'image_thumb')
"""        
	def image_thumb(self, obj):
		if obj.image(self, obj):
		    thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
		    return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
		else:
		    return "No Image" 
        image_thumb.short_description = 'Cover Image'
        image_thumb.allow_tags = True

"""	
admin.site.register(CategoryImage ,CategoryImageAdmin)
admin.site.register(Category ,CategoryAdmin)

 
