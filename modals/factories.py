import random
import string
import factory

from models import Modal


class ModalFactory(factory.Factory):
    
    class Meta:
        model = Modal

    title = factory.Sequence(lambda n: 'Modal%d' % n)
    enabled = random.random < 0.3
    is_bootstrapped = random.random < 0.3
