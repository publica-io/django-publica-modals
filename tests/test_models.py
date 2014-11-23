#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-publica-modals
------------

Tests for `django-publica-modals` models module.
"""

import os
import shutil
import unittest

from django.db.models import Model
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext

from modals import models
from modals.templatetags.modals_tags import bootstrapped_modals
from templates.models import Template
from images.models import Image, ImageInstance
from models import Modalable

class TestModals(unittest.TestCase):

    def setUp(self):
        self.t1, _ = Template.objects.get_or_create(
            name='modals/modal_detail.html', content='Does it matter')

         # Create the Image
        self.popup_image1, created = Image.objects.get_or_create(
            title='Popup Image',
            url='/img/test.jpg'
        )

        self.popup_image2, created = Image.objects.get_or_create(
            title='Popup Image',
            url='/img/test.jpg'
        )

        self.modal1, _ = models.Modal.objects.get_or_create(enabled=True, title='Home Popup',
                                                           template=self.t1, is_bootstrapped=True,
                                                           text='This is going to be modal text')

        self.modal2, _ = models.Modal.objects.get_or_create(enabled=True, title='Home Popup2',
                                                           template=self.t1, is_bootstrapped=True,
                                                           text='This is going to be modal text')

        # Add Image to Modal via ImageInstance
        self.image_instance, _ = ImageInstance.objects.get_or_create(
            image=self.popup_image1,
            content_type=ContentType.objects.get_for_model(models.Modal),
            object_id=self.modal1.pk,
            enabled=True,
        )

        # Add Image to Modal via ImageInstance
        self.image_instance, _ = ImageInstance.objects.get_or_create(
            image=self.popup_image1,
            content_type=ContentType.objects.get_for_model(models.Modal),
            object_id=self.modal2.pk,
            enabled=True,
        )
        # create my mock modelable object
        self.modalable = Modalable()
        self.modalable.save()

        self.modalAspect, _ = models.ModalAspect.objects.get_or_create(
            modal=self.modal1,
            content_type=ContentType.objects.get_for_model(self.modalable),
            object_id=self.modalable.pk,
        )

        self.modalAspect, _ = models.ModalAspect.objects.get_or_create(
            modal=self.modal2,
            content_type=ContentType.objects.get_for_model(self.modalable),
            object_id=self.modalable.pk,
        )

    def test_modals_tag(self):
         self.assertTrue(self.modal1.text in bootstrapped_modals(context=RequestContext({}), slug='home-popup'))
         self.assertTrue(self.modal2.text in bootstrapped_modals(context=RequestContext({}), slug='home-popup2'))

    def test_modals_get_modal_by_slug(self):
        self.assertEqual(self.modalable.get_modal_by_slug('home-popup'), self.modal1)
        self.assertEqual(self.modalable.get_modal_by_slug('home-popup2'), self.modal2)


    def tearDown(self):
        pass
