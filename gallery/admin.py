from django.utils.safestring import mark_safe
from django.contrib import admin
from gallery.models import *

class GalleryImageAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',)}
	list_display = ('id', 'image_category', 'date_created' ,'is_publish','image')
        list_filter = ('image_category', 'is_publish')
        

class ImageCategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'category_image', 'date_created')
        
	
admin.site.register(GalleryImage ,GalleryImageAdmin)
admin.site.register(ImageCategory ,ImageCategoryAdmin)

 
