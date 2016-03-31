import json
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_filer_gallery.models import FilerGallery, QUALITY_SIZE
from cmsplugin_filer_gallery.models import ANIMATION_CHOICES
import django

from cmsplugin_filer_gallery.admin import ImageInline


class FilerGalleryPlugin(CMSPluginBase):
    model = FilerGallery
    name = _("Filer Gallery")
    render_template = "cmsplugin_filer_gallery/gallery.html"
    text_enabled = True
    raw_id_fields = ('gallery',)
    admin_preview = False,
    inlines = [ImageInline, ]
    if django.VERSION[1] > 4:
        change_form_template = "cmsplugin_filer_gallery/plugin_change.html"
    else:
        change_form_template = "cmsplugin_filer_gallery/plugin_change_old.html"

    def render(self, context, instance, placeholder):
        config = json.dumps({
            'transition': ANIMATION_CHOICES[instance.animation][1],
            'initialTransition': ANIMATION_CHOICES[instance.first_animation][1],
            'height': instance.height,
            'width': instance.width,
            'lightbox': instance.lightbox,
            'imagePan': True,
            'autoplay': instance.autoplay,
            'autoplay_timeout': instance.autoplay_timeout,
            'imagecrop': instance.imagecrop,
        }
        )

        context.update({
            'instance': instance,
            'size': self._get_size_options(context, instance),
            'config': config
        })
        return context

    def _get_size_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        retval = dict()

        width, height = instance.width, instance.height
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)

        if width:
            retval.update({'width': width})
        elif placeholder_width:
            retval.update({'width': placeholder_width})

        if height:
            retval.update({'height': height})
        elif placeholder_width:
            retval.update({'height': placeholder_height})

        retval.update({'thumb_size': QUALITY_SIZE[instance.quality]})


        return retval


plugin_pool.register_plugin(FilerGalleryPlugin)
