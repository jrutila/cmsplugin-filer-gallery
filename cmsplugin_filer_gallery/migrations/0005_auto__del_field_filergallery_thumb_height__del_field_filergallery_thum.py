# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FilerGallery.thumb_height'
        db.delete_column('cmsplugin_filergallery', 'thumb_height')

        # Deleting field 'FilerGallery.thumb_width'
        db.delete_column('cmsplugin_filergallery', 'thumb_width')

        # Deleting field 'FilerGallery.animate_number_active'
        db.delete_column('cmsplugin_filergallery', 'animate_number_active')

        # Adding field 'FilerGallery.first_animation'
        db.add_column('cmsplugin_filergallery', 'first_animation',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FilerGallery.autoplay_active'
        db.add_column('cmsplugin_filergallery', 'autoplay_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FilerGallery.autoplay_timeout'
        db.add_column('cmsplugin_filergallery', 'autoplay_timeout',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=3000),
                      keep_default=False)

        # Adding field 'FilerGallery.lightbox'
        db.add_column('cmsplugin_filergallery', 'lightbox',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FilerGallery.thumb_height'
        db.add_column('cmsplugin_filergallery', 'thumb_height',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FilerGallery.thumb_width'
        db.add_column('cmsplugin_filergallery', 'thumb_width',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FilerGallery.animate_number_active'
        db.add_column('cmsplugin_filergallery', 'animate_number_active',
                      self.gf('django.db.models.fields.CharField')(default='#FF0000', max_length=7),
                      keep_default=False)

        # Deleting field 'FilerGallery.first_animation'
        db.delete_column('cmsplugin_filergallery', 'first_animation')

        # Deleting field 'FilerGallery.autoplay_active'
        db.delete_column('cmsplugin_filergallery', 'autoplay_active')

        # Deleting field 'FilerGallery.autoplay_timeout'
        db.delete_column('cmsplugin_filergallery', 'autoplay_timeout')

        # Deleting field 'FilerGallery.lightbox'
        db.delete_column('cmsplugin_filergallery', 'lightbox')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 29, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_filer_gallery.filergallery': {
            'Meta': {'object_name': 'FilerGallery', 'db_table': "'cmsplugin_filergallery'", '_ormbases': ['cms.CMSPlugin']},
            'animation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'autoplay_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autoplay_timeout': ('django.db.models.fields.SmallIntegerField', [], {'default': '3000'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'first_animation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer_gallery.Gallery']"}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {'default': '200', 'null': 'True', 'blank': 'True'}),
            'lightbox': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'default': '300', 'null': 'True', 'blank': 'True'})
        },
        'filer_gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_filer_gallery']