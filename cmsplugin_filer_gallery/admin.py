from django.contrib import admin
from cmsplugin_filer_gallery.models import GalleryImage

class ImageInline(admin.TabularInline):
    model = GalleryImage
