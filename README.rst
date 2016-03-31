cmsplugin-filer-gallery 
=======================

This is add-on for django-cms. It's built on filer-gallery, but dows not rely anything else than database models. Aim of this branch is to make easy to use as possible gallery element for Django-cms. So there should be no reason to go admin, all shoud be possible straign from front-end editing.

Gallery
-------

We use nce javascrip gallery from https://github.com/aino/galleria. Galleria has tons of settings and supports themes (one free theme available). At this point only some settings can be modified from cms.

Installing
==========

add 'cmsplugin_filer_gallery' to INSTALLED_APPS, you have now new plugin in django-cms.

Requirements
------------

django-filer
cmsplugin-filer
filer-gallery

