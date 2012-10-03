from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_filer_gallery.models import FilerGallery
from cmsplugin_filer_gallery.models import ANIMATION_CHOICES

class FilerGalleryPlugin(CMSPluginBase):
    model = FilerGallery
    name = _("Filer Gallery")
    render_template = "cmsplugin_filer_gallery/gallery.html"
    text_enabled = False
    raw_id_fields = ('gallery',)
    admin_preview = False,
    change_form_template="cmsplugin_filer_gallery/plugin_change.html"
    
    def render(self, context, instance, placeholder):
        config = simplejson.dumps({
            'animation': ANIMATION_CHOICES[instance.animation][1],
            'height': instance.height,
            'width': instance.width,
            'lightbox': True,
            }
        )
        context.update({
            'instance': instance,
            'size': (instance.width, instance.height),
            'thumb_size': (instance.thumb_height, instance.thumb_width),
            'skitter_config': config
        })
        return context

plugin_pool.register_plugin(FilerGalleryPlugin)