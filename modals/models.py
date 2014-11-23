
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

    pass

