from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_filer_gallery.models import FilerGallery
from cmsplugin_filer_gallery.models import ANIMATION_CHOICES

from cmsplugin_filer_gallery.admin import ImageInline

class FilerGalleryPlugin(CMSPluginBase):
    model = FilerGallery
    name = _("Filer Gallery")
    render_template = "cmsplugin_filer_gallery/gallery.html"
    text_enabled = True
    raw_id_fields = ('gallery',)
    admin_preview = False,
    inlines = [ImageInline, ]
    change_form_template="cmsplugin_filer_gallery/plugin_change.html"
    
    def render(self, context, instance, placeholder):
        config = simplejson.dumps({
            'transition': ANIMATION_CHOICES[instance.animation][1],
            'initialTransition': ANIMATION_CHOICES[instance.first_animation][1],
            'height': instance.height,
            'width': instance.width,
            'lightbox': instance.lightbox,
            'imagePan' :True,
            'autoplay' : instance.autoplay,
            }
        )
        
        context.update({
            'instance': instance,
            'size': self._get_size_options(context,instance),
            'config': config
        })
        return context


    def _get_size_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        retval=dict()
        
        width, height = instance.width, instance.height
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)
        
        if width:
            retval.update({'width':width})
        elif placeholder_width:
            retval.update({'width':placeholder_width})
        else:
            retval.update({'width':200})
            

        if height:
            retval.update({'height':height})
        elif placeholder_width:
            retval.update({'height':placeholder_height})
        else:
            retval.update({'height':200})
       
        
        thumb_size = str(retval['width']-20) +'x'+ str(retval['height']-70)
        
        retval.update({'thumb_size': thumb_size})
        
        return retval


plugin_pool.register_plugin(FilerGalleryPlugin)