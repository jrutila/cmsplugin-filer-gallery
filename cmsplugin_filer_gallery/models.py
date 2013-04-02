# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from positions.fields import PositionField

from datetime import datetime
from filer.fields.image import FilerImageField
ANIMATION_CHOICES=('fade','flash','pulse','slide', 'fadeslide')
ANIMATION_CHOICES=tuple(enumerate(ANIMATION_CHOICES))


class FilerGallery(CMSPlugin):

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
    
    class Meta:
        verbose_name = _("django filer gallery")
        verbose_name_plural = _("django filer galleries")
        
        
        
class GalleryImage(models.Model):
    gallery = models.ForeignKey(FilerGallery, related_name="images")
    image = FilerImageField(related_name="imagesss")
    active = models.BooleanField(_('Active'), default=True)
    pub_date = models.DateTimeField(default=datetime.now)   
    order = models.IntegerField(default=1)
    ordering = PositionField(collection='gallery')
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')

    def __unicode__(self):
        """Return the FilerImage name"""
        return u"%s" % self.image

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pub_date = self.image.date_taken
        super(GalleryImage, self).save(*args, **kwargs)