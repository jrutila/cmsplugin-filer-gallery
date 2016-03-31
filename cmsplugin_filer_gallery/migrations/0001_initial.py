# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import datetime
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('animation', models.SmallIntegerField(default=0, verbose_name='animation', choices=[(0, b'fade'), (1, b'flash'), (2, b'pulse'), (3, b'slide'), (4, b'fadeslide')])),
                ('first_animation', models.SmallIntegerField(default=0, verbose_name='first image animation', choices=[(0, b'fade'), (1, b'flash'), (2, b'pulse'), (3, b'slide'), (4, b'fadeslide')])),
                ('quality', models.SmallIntegerField(default=1, verbose_name='Image quality', choices=[(0, b'low'), (1, b'normal'), (2, b'high')])),
                ('height', models.SmallIntegerField(default=300, help_text='Height of gallery', null=True, verbose_name='Gallery height', blank=True)),
                ('width', models.SmallIntegerField(default=None, help_text='Leave empty for auto width', null=True, verbose_name='Gallery width', blank=True)),
                ('autoplay_active', models.BooleanField(default=False, help_text='Start playing automatically', verbose_name='autoplay')),
                ('autoplay_timeout', models.SmallIntegerField(default=3000, help_text='Timeout for next picture in ms', verbose_name='autoplay timeout')),
                ('lightbox', models.BooleanField(default=True, help_text='show fullscreen image in lightbox', verbose_name='lightbox')),
                ('imagecrop', models.BooleanField(default=False, help_text='If selected image will be cropped', verbose_name='ImageCrop')),
                ('theme', models.CharField(default=b'classic', help_text='Theme for current gallery', max_length=10, choices=[(b'classic', b'classic'), (b'miniml', b'miniml')])),
            ],
            options={
                'verbose_name': 'django filer gallery',
                'verbose_name_plural': 'django filer galleries',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('ordering', positions.fields.PositionField(default=-1)),
                ('gallery', models.ForeignKey(related_name='images', to='cmsplugin_filer_gallery.FilerGallery')),
                ('image', filer.fields.image.FilerImageField(related_name='imagesss', to='filer.Image')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
    ]
