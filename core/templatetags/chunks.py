import itertools

from django import template

register = template.Library()


@register.filter
def chunks(value, chunk_length):
    """
    Breaks a list up into a list of lists of size <chunk_length>
    """
    clean = int(chunk_length)
    i = iter(value)
    while True:
        chunk = list(itertools.islice(i, clean))
        if chunk:
            yield chunk
        else:
            break
