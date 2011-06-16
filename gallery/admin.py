from django.utils.safestring import mark_safe
from django.contrib import admin
from gallery.models import *
from sorl.thumbnail import *
ADMIN_THUMBS_SIZE = '60x60'

class CategoryImageAdmin(admin.ModelAdmin):
	
	prepopulated_fields={'slug':('title',)}
	list_display = ('order','title', 'image_category', 'date_created' ,'is_publish') #,'my_image_thumb')
        list_filter = ('image_category', 'is_publish')
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

 
