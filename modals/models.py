from django.db import models
from django.db.models.loading import get_model
from django.contrib.contenttypes.models import ContentType

from polymorphic import PolymorphicModel
from entropy.mixins import (
    TextMixin, EnabledMixin, SlugMixin, TitleMixin
)
from attrs.mixins import GenericAttrMixin
from templates.mixins import TemplateMixin

try:
    from images.mixins import ImageMixin
except ImportError:
    ImageMixin = object


# Modal Base Classes

class Modal(PolymorphicModel, GenericAttrMixin, EnabledMixin, SlugMixin,
            TextMixin, TitleMixin, TemplateMixin, ImageMixin):


    @property
    def links(self):
        return [modal_link.link for modal_link in self.aspects.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(
                get_model('modals.ModalLinkAspect')
            )
        )]

    @property
    def link(self):
        try:
            return self.links[0]
        except IndexError:
            return None


class ModalAspect(PolymorphicModel, TitleMixin, TextMixin, SlugMixin, ImageMixin):

    modal = models.ForeignKey('Modal', related_name='aspects')


# Modal link aspect

class ModalLinkAspect(ModalAspect):
    '''
    Create a linkage to a menus.Link
    '''

    link = models.ForeignKey('menus.Link')
