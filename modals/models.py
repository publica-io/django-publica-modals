from django.db import models
from django.contrib.contenttypes import generic

from polymorphic import PolymorphicModel
from entropy.mixins import (
    TextMixin, EnabledMixin, SlugMixin, TitleMixin
)
from attrs.mixins import GenericAttrMixin
from templates.mixins import TemplateMixin

from .settings import CONTENT_MODELS

try:
    from images.mixins import ImageMixin
except ImportError:
    ImageMixin = object


# Modal Base Classes

class Modal(PolymorphicModel, GenericAttrMixin, EnabledMixin, SlugMixin,
            TextMixin, TitleMixin, TemplateMixin, ImageMixin):

    is_bootstrapped = models.BooleanField(default=False)

    # def get_slug(self):
    #     return self.slug if self.slug else ''


class ModalAspect(PolymorphicModel, EnabledMixin):

    modal = models.ForeignKey('Modal')
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        limit_choices_to={'model__in': CONTENT_MODELS},
    )
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

