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
from menus.models import Link



class TestModalLinks(unittest.TestCase):

    def setUp(self):
        
        self.modal = models.Modal(
            title = 'foo',
            slug = 'foo')
        self.modal.save()

        self.link = Link(
            url='/some/funky/url')
        self.link.save()

        self.modal_link = models.ModalLinkAspect(
            modal=self.modal,
            link=self.link)
        self.modal_link.save()
        

    def test_links(self):

        list_urls = [link.get_url() for link in self.modal.links]
        self.assertEqual(list_urls, [u'/some/funky/url'])

    def test_link(self):
        self.assertEqual(self.modal.link.get_url(), '/some/funky/url')

    def test_no_links(self):
        self.modal_link.delete()
        self.link.delete()

        self.assertEqual(self.modal.links, [])
        self.assertEqual(self.modal.link, None)
