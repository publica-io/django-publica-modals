from django import template
from ..models import Modal


register = template.Library()


@register.simple_tag(takes_context=True)
def bootstrap_modal(context, slug):
    try:
        modal = Modal.objects.get(slug=slug)
    except Modal.DoesNotExist:
        return ''
    else:
        return modal.render(context)