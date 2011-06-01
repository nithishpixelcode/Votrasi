# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'GalleryImages.is_publish'
        db.delete_column('gallery_galleryimages', 'is_publish')

        # Adding field 'GalleryImages.is_published'
        db.add_column('gallery_galleryimages', 'is_published', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'GalleryImages.is_publish'
        db.add_column('gallery_galleryimages', 'is_publish', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Deleting field 'GalleryImages.is_published'
        db.delete_column('gallery_galleryimages', 'is_published')


    models = {
        'gallery.galleryimages': {
            'Meta': {'object_name': 'GalleryImages'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('widgets.RemovableImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.ImageCategory']"}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'gallery.imagecategory': {
            'Meta': {'object_name': 'ImageCategory'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['gallery']
