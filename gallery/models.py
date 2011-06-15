from django.db import models
from widgets import RemovableImageField
from datetime import datetime
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^widgets\.RemovableImageField"])

class ImageCategory(models.Model):
    
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    cat_info =models.TextField(null=False)
    name = models.CharField(max_length=30,  unique=True)
    category_image = RemovableImageField(upload_to='images/upload/catimg', null=True, blank=True)
    
    class Meta:
        ordering = ['id',]
        
    def __unicode__(self):
      
        return self.name 
        
    def get_absolute_url(self):
        return '%s/' % (self.slug)

class GalleryImage(models.Model):
   
    title  = models.CharField(max_length=20, unique=True)
    slug= models.SlugField(unique=True)
    img_info =models.TextField(null=True)
    order = models.IntegerField(null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True)
    is_publish = models.BooleanField(default=True)
    image_category= models.ForeignKey('ImageCategory', to_field='name')  
    image = RemovableImageField(upload_to='images/upload', null=True, blank=True)
    
    class Meta:
        ordering = ['order',]
        
    def __unicode__(self):
       
        return self.title;
        
    def get_absolute_url(self):
        return '%s/' % (self.slug)


