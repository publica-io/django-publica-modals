from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from django.db import models
from .models import ModalAspect


class ModalMixin(object):
    '''
    So the Mixin can be imported into any type of Model
    '''

    @cached_property
    def qset(self):
        return ModalAspect.objects.filter(
            object_id=self.pk,
            content_type=ContentType.objects.get_for_model(self)
        )

    @property
    def modals(self):
        '''Return all the images'''
        return self.qset

    @property
    def modal(self):
        return self.modals.first()

    def get_modal_by_slug(self, slug):
        return self.modals.filter(modal__slug=slug).first().modal if self.modals.filter(modal__slug=slug).first().modal else ''
