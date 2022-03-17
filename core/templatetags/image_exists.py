import os

from django import template

register = template.Library()


@register.simple_tag(name='image_exists')
def image_exists(path):
    if os.path.isfile(path):
        return path
    else:
        return "/media/services/default.png"
