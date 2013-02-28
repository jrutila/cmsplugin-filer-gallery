# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FilerGallery.height'
        db.alter_column('cmsplugin_filergallery', 'height', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'FilerGallery.width'
        db.alter_column('cmsplugin_filergallery', 'width', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'FilerGallery.animate_number_active'
        db.alter_column('cmsplugin_filergallery', 'animate_number_active', self.gf('django.db.models.fields.CharField')(max_length=7))

    def backwards(self, orm):

        # Changing field 'FilerGallery.height'
        db.alter_column('cmsplugin_filergallery', 'height', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'FilerGallery.width'
        db.alter_column('cmsplugin_filergallery', 'width', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'FilerGallery.animate_number_active'
        db.alter_column('cmsplugin_filergallery', 'animate_number_active', self.gf('django.db.models.fields.CharField')(max_length=6))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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
            'animate_number_active': ('django.db.models.fields.CharField', [], {'default': "'#FF0000'", 'max_length': '7'}),
            'animation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer_gallery.Gallery']"}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {'default': '200', 'null': 'True', 'blank': 'True'}),
            'thumb_height': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'thumb_width': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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