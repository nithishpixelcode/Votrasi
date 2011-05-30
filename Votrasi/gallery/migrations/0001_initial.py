# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'GalleryImages'
        db.create_table('gallery_galleryimages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('html_metakey', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('html_metadata', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.ImageCategory'])),
            ('image', self.gf('widgets.RemovableImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['GalleryImages'])

        # Adding model 'ImageCategory'
        db.create_table('gallery_imagecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('html_metakey', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('html_metadata', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('category_image', self.gf('widgets.RemovableImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['ImageCategory'])


    def backwards(self, orm):
        
        # Deleting model 'GalleryImages'
        db.delete_table('gallery_galleryimages')

        # Deleting model 'ImageCategory'
        db.delete_table('gallery_imagecategory')


    models = {
        'gallery.galleryimages': {
            'Meta': {'object_name': 'GalleryImages'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'html_metadata': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'html_metakey': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('widgets.RemovableImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.ImageCategory']"}),
            'is_publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'gallery.imagecategory': {
            'Meta': {'object_name': 'ImageCategory'},
            'category_image': ('widgets.RemovableImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'html_metadata': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'html_metakey': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['gallery']
