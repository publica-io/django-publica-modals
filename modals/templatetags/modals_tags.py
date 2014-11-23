from django import template
from ..models import Modal


register = template.Library()


@register.simple_tag(takes_context=True)
def bootstrapped_modals(context):
    '''
    Render all the Modals on the page that are marked `is_bootstrapped = True`
    '''

    modals = Modal.objects.filter(is_bootstrapped=True)

    html = []
    for modal in modals:
        html.append(modal.render(context))

    return ''.join(html)
