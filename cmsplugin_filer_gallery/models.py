# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page

ANIMATION_CHOICES=('fade','flash','pulse','slide', 'fadeslide')
ANIMATION_CHOICES=tuple(enumerate(ANIMATION_CHOICES))

CAPTION_ANIMATION_CHOICES=('fade', 'slideOpen')
CAPTION_ANIMATION_CHOICES=tuple(enumerate(CAPTION_ANIMATION_CHOICES))

class FilerGallery(CMSPlugin):

    gallery = models.ForeignKey('filer_gallery.Gallery')

    animation = models.SmallIntegerField(_("animation"), choices=ANIMATION_CHOICES, default=0)
    first_animation = models.SmallIntegerField(_("first image animation"), choices=ANIMATION_CHOICES, default=0)
    

    height = models.SmallIntegerField(_("height"),default=200,
                                      null=True, blank=True,
                                      help_text=_('Leave empty for auto width'))
    width = models.SmallIntegerField(_("width"), default=300,
                                     null=True, blank=True,
                                     help_text=_('Leave empty for auto width'))
    autoplay_active = models.BooleanField(_("autoplay"), default=False,
                                    help_text=_('Start playing automatically'))
    
    autoplay_timeout = models.SmallIntegerField(_("autoplay timeout"), default=3000,
                                    help_text=_('Timeout for next picture in ms'))
    lightbox = models.BooleanField(_("lightbox"), default=True,
                                    help_text=_('show fullscreen image in lightbox'))
    
    @property
    def autoplay(self):
        if not self.autoplay_active:
            return False
        return self.autoplay_timeout
        
    @property
    def size_x(self):
        # size for thmbnailer to use for images widthxheight
        size = str(self.width-20)+'x'+ str(self.height-70)
        return size
    
    class Meta:
        verbose_name = _("django filer gallery")
        verbose_name_plural = _("django filer galleries")