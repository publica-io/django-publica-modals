from django.db.models import Model
from modals import mixins


class Modalable(Model, mixins.ModalMixin):
    pass
