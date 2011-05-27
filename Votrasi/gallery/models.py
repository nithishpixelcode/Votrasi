from django.db import models
import os
from widgets import RemovableImageField
from datetime import datetime

#We need to tell south what migration rules is needed for our custom field
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^widgets\.RemovableImageField"])

class GalleryImages(models.Model):
    """
        Inserting  a single image to the Category
    """
    title           = models.CharField(max_length=20, unique=True)
    slug            = models.SlugField(unique=True)
    order           = models.IntegerField(null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True)
    is_publish      = models.BooleanField(default=True)
    image_category  = models.ForeignKey('ImageCategory')
    image           = RemovableImageField(upload_to='images/upload', null=True, blank=True)
    
    
    def __unicode__(self):
        """
        When referencing the GalleryImages object, return its name.
        
        @rtype: string
        @return: The name of the gallery.
        """
        return self.title;
    
    def delete(self):
        """
        Deletes the image in the database and from the file system.
        """
        try:
            os.remove(self.image)
        except:
            pass
        
    def get_absolute_url(self):
        return '%s/' % (self.slug)
    

    
    
class ImageCategory(models.Model):
    """
        Cerate new category
    """
    
    date_created    = models.DateTimeField(auto_now_add=True)
    title           = models.CharField(max_length=20, unique=True)
    slug            = models.SlugField(unique=True)
    category_name   = models.CharField(max_length=30)
    category_image  = RemovableImageField(upload_to='images/upload/catimg', null=True, blank=True)
    
    
    def __unicode__(self):
        """
        When referencing the GalleryImages object, return its name.
        
        @rtype: string
        @return: The name of the gallery.
        """
        return self.category_name;
    def get_absolute_url(self):
        return '%s/' % (self.slug)
    
